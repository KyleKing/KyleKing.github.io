Meteor.publish 'DailyBikeDataPub', ->
  DailyBikeData.find()