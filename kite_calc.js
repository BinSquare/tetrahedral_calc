if (Meteor.isClient) {
  Template.calculate.events({
    'submit form': function (event, template) {
      // calculating for the 
      var num_layer = event.target.layer_numbers.value;
      session.set('num_layer', num_layer)
      console.log(num_layer)
    }
  });
  Template.calculate.helpers({
    var layer = session.get(numlayer)
    
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
