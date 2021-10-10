// Node.js on PC
const SerialPort = require('serialport'); // npm i serialport
const Readline = require('@serialport/parser-readline');

let comPort = 'COM3'; // from device manager
let baudrate = 9600;

const port = new SerialPort(comPort, { baudRate: baudrate });
const parser = port.pipe(new Readline({ delimiter: '\n' }));


port.on('open', () => {
    console.log('COM-Port is now open!');
});

parser.on('data', data =>{
    console.log('Message from Microcontroller: ' + data)
});

/********************************************************* */

sendCommand('on()'); //turn LED on

setTimeout(function(){ //turn LED in 2 Seconds off 
    sendCommand('off()');
}, 2000);


setTimeout(function(){ //close Port after 2.1 Seconds 
    port.close(function () {
        console.log('port closed');
    })
}, 2100);


/********************************************************* */

function sendCommand(comm){ // command must be formatted before it is sent to the microcontroller
    comm = comm + '\r\f'
    port.write(unescape(encodeURIComponent(comm))); // encode_utf8 and send to microcontroller
}
