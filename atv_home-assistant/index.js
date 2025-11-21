const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const mqtt = require('mqtt');

const MQTT_BROKER_IP = "mqtt://X.X.X.X"; 
const MQTT_TOPIC = "homeassistant/minecraft/notificacao";

const MQTT_USERNAME = ""; 
const MQTT_PASSWORD = ""; 

let MEU_CELULAR_ID = ""; 

const mqttOptions = {
    username: MQTT_USERNAME,
    password: MQTT_PASSWORD
};

const mqttClient = mqtt.connect(MQTT_BROKER_IP, mqttOptions);


//Cliente MQTT
mqttClient.on('error', (error) => {
    console.error('Erro na conexão MQTT:', error);
});

mqttClient.on('connect', () => {
    console.log('✅ Conectado ao Broker MQTT');
    
    mqttClient.subscribe(MQTT_TOPIC, (err) => {
        if (!err) {
            console.log(`✅ Inscrito no tópico: ${MQTT_TOPIC}`);
        } else {
            console.error('❌ Falha ao se inscrever no tópico:', err);
        }
    });
});

// Cliente WhatsApp
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

client.on('qr', (qr) => {
    console.log('QR Code recebido, escaneie com seu celular:');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('✅ Cliente WhatsApp está pronto!');

    // pega o id do usuario
    MEU_CELULAR_ID = client.info.wid._serialized;
    
    console.log("✅ Sistema de Alerta Minecraft Ativado!");
    client.sendMessage(MEU_CELULAR_ID, "✅ Sistema de Alerta Minecraft Ativado!");
});


//Alerta por Wpp
mqttClient.on('message', (topic, message) => {
    if (topic === MQTT_TOPIC) {
        const msgTexto = message.toString();        
        if (MEU_CELULAR_ID) {
            try {
                client.sendMessage(MEU_CELULAR_ID, `🚨 *ALERTA MINECRAFT*\n\n${msgTexto}`);
            } catch (error) {
                console.error("❌ Erro ao tentar enviar mensagem:", error);
            }
        } else {
            console.warn('❌ WhatsApp falhou. Alerta perdido.');
        }
    }
});

// Inicializa o bot
client.initialize();