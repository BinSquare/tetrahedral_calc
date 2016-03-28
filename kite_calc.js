layer_dump = new Mongo.Collection('layers');

if (Meteor.isClient) {
  Template.body.events({
    'submit .ask': function (event) {
      // calculating for the 
      var num_layer = event.target.layer.value;
      console.log(event)
      console.log(num_layer)
      layer_dump.insert({
        layers : num_layer
      })
    }
  });
  Template.body.helpers({
    module_num: layers
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
