var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');
var bot_info = require('./package.json');
var settings = require('./settings.json');
var mysql = require('mysql');

//Mysql moduulin yhdistäminen tietokantaan

var con = mysql.createConnection({
  host: "localhost",
  user: "test_user",
  password: "test_password",
  database:"panttibotti"
});

con.connect(function(err){
  if(err) throw err;
  console.log("Connected!");
});

con.query('Select * from panttitieto', function (error, results, fields){
  console.log(results);
});

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
    colorize: true
});
logger.level = 'debug';
// Initialize Discord Bot
var bot = new Discord.Client({
   token: auth.token,
   autorun: true,
   messageCacheLimit:0
});
bot.setPresence({ game:{name:'ElämämPeli'}});
bot.on('ready', function (evt) {
    logger.info('PanttiBotti ready for duty');
    bot.sendMessage({
      to: settings.bot_channel_id,
      message: ' Hello everyone! My name is ' + bot_info.name + '. \n'
              +"please use '!help' to see what functions I am capable of performing \n"
    });
});

bot.on('message', function (user, userID, channelID, message, evt) {
    // Our bot needs to know if it will execute a command
    // It will listen for messages that will start with `!`
    if (message.substring(0, 1) == '!') {
        var args = message.substring(1).split(' ');
        logger.info (args);
        var cmd = args[0];

        args = args.splice(1);
        switch(cmd) {

            case 'intro':
                bot.sendMessage({
                    to: channelID,
                    message: 'Hello ' + user +' My name is ' + bot_info.name
                    + '. I am tracking your bottle deposits and their value.'
                });
            break;

            case 'value':
                con.query('Select round(sum(pantti),2) as luku from panttitieto', function (error, results, fields){
                  deposit_value = results[0].luku;
                  if(deposit_value == null){
                    deposit_value = 0;
                  }
                  bot.sendMessage({
                  to: channelID,
                  message: 'Value of the deposits is: ' + deposit_value +' €'
                  });
                });
           break;

           case 'bottles':
           con.query('Select count(*) as lkm from panttitieto', function (error, results, fields){
             deposit_amount = results[0].lkm;
             if(deposit_amount == null)
             {
               deposit_amount = 0;
             }
               bot.sendMessage({
               to: channelID,
               message: 'You have depositted ' + deposit_amount + ' bottles'
               });
             });
          break;

          case 'clear':
          con.query('truncate table panttitieto;',function (error, results, fields){
              bot.sendMessage({
              to: channelID,
              message: 'Deposits and their total value have been set back to 0 '
              });
            })
         break;

           case 'help':
               bot.sendMessage({
               to: channelID,
               message: 'All available commands:\n \n'
                        +'!intro:\t introduces the bot and tells it purpose \n\n'
                        +'!value:\t The bot tells you the value of your bottle deposits \n\n'
                        +'!bottles:\t The bot tells you the amount of bottles you have deposited\n\n'
                        +'!clear:\t Use this to reset the bot in case you have emptyed the bottle holder\n\n'
                        +'!exit: \t This command shutsdown the bot and makes it disconnect from the server\n\n'
               });
          break;

          case 'exit':
              process.exit();
         }
     }
});
