var Minicom = {

  register: function(user_email, text_div) {
    $.post('http://localhost:8000/api/ping', {'email': user_email})
    .done(function(response) {
      $.each(response['unread_messages'], function(index, message) {
        alert(message.message);
        Minicom.mark_read(user_email, message.message_id);
      });
        text_div.val(response['unread_messages'].map(function(message) {return ("--" + message.message)}));
    });
  },

  mark_read: function(user_email, message_id) {
    $.post('http://localhost:8000/api/read', {'email': user_email, 'message_id': message_id});
  },
    
  send_admin: function(user_email, message_text) {
    $.post(
        'http://localhost:8000/api/send_admin',
        {'email': user_email, 'message_text': message_text}
    )
    .done(function(response) {
      $.each(response['unread_messages'], function(index, message) {
        alert(message.message);
        Minicom.mark_read(user_email, message.message_id);
      });
    });
  },

};
