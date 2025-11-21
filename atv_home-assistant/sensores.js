const mqtt = require('mqtt');

const MQTT_BROKER_IP = "mqtt://192.168.1.6";
const MQTT_USERNAME = "bot_mqtt";
const MQTT_PASSWORD = "123456";

const TOPIC_TEMPERATURA = "homeassistant/sensor/virtual_temp";
const TOPIC_UMIDADE =     "homeassistant/sensor/virtual_umidade";

const INTERVALO = 5000; // 5 seg


const mqttOptions = {
    username: MQTT_USERNAME,
    password: MQTT_PASSWORD
};

const mqttClient = mqtt.connect(MQTT_BROKER_IP, mqttOptions);

mqttClient.on('error', (error) => {
    console.error('Erro na conexão MQTT:', error);
});

//loop de publicar dados
mqttClient.on('connect', () => {    
    setInterval(publicarDados, INTERVALO);
});

function publicarDados() {
    // 18 a 26C
    var temperatura = (Math.random() * 8 + 18).toFixed(1); 
    
    // 40 a 71C
    var umidade = (Math.floor(Math.random() * 31) + 40).toString();

    mqttClient.publish(TOPIC_TEMPERATURA, temperatura);
    mqttClient.publish(TOPIC_UMIDADE, umidade);

     console.log(`U: ${umidade} % | T: ${temperatura}°C`);

}
