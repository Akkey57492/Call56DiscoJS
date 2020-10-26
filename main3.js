const Discord = require("discord.js"); //　discord.js
const client = new Discord.Client()
let prefix = ">" // Prefix指定

client.on("message", message => { // メッセージを受け取ったときに処理を行う
  if (message.author.bot) { // Botのメッセージは除外
    return;
  }
  if (message.content == prefix + "ping") { // コマンド
    message.channel.send( // メッセージを送信
  {embed: { // Embed
    title: "Ping測定", // Embedのタイトル
    description: "Ping"+client.ws.ping+"ms", // Embedの内容
  }}
);
  }
  if (message.content.match(/おは/)) { // メッセージ
    message.channel.send("おはよう。あーだる。俺はトイレ行ってもう一度寝るわ。") // メッセージ送信
  }
    if (message.content.match(/おや/)) { // メッセージ
    message.channel.send("おやすみ。あ、俺は後で寝るわ。電気消したくないから頑張って明るいまま寝てくんね?") // メッセージ送信
  }
    if (message.content.match(/@everyone/)) { // メッセージ
    message.channel.send("うるせぇよ。今ゲームに集中してるんだよ。") // メッセージ送信
  }
    if (message.content.match(/@here/)) { // メッセージ
    message.channel.send("うるせぇよ。今ゲームに集中してるんだよ。") // メッセージ送信
  }
    if (message.content.match(/雑魚/)) { // メッセージ
    message.channel.send("そんな煽りしかできないのかなぁー?www") // メッセージ送信
  }
    if (message.content.match(/ざこ/)) { // メッセージ
    message.channel.send("そんな煽りしかできないのかなぁー?www") // メッセージ送信
  }
});

client.login('Token') // Token
