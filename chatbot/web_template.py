css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/919106726/vector/vector-robot-flat-icon.jpg?s=612x612&w=0&k=20&c=9GousaHRCnd9hvV7UYqjEj9YwXRuNSZhFb1xhwbNrqM=" style="max-height: 80px; max-width: 80px; border="20" >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://t3.ftcdn.net/jpg/05/79/55/26/360_F_579552668_sZD51Sjmi89GhGqyF27pZcrqyi7cEYBH.jpg" style="max-height: 100px; max-width: 80px; border="20" >
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''