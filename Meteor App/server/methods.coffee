Meteor.methods 'DeleteOldBikes': ->
  # Useful function from lib/CurrentDay.coffee for current date and time
  [today, now] = CurrentDay()
  today = today + 1
  DailyBikeData.remove({ Day: { $lt:  today} })
  CreateDailyBikeData()
  'ok'

# CreateDailyBikeData()