[today, now] = CurrentDay()

CreateDailyBikeData = () ->

  randNames = [
    'Anastasia Romanoff'
    'Marie Antoinette'
    'Chuff Chuffington'
    'Kate Middleton'
    'Harry Potter'
    'Snow White'
    'Lake Likesscooters'
    'Pippa Middleton'
    'Napoleon Bonapart'
    'Britany Bartsch'
    'Roselee Sabourin'
    'Chelsie Vantassel'
    'Chaya Daley'
    'Luella Cordon'
    'Jamel Brekke'
    'Jonie Schoemaker'
    'Susannah Highfield'
    'Mitzi Brouwer'
    'Forrest Lazarus'
    'Dortha Dacanay'
    'Delinda Brouse'
    'Alyssa Castenada'
    'Carlo Poehler'
    'Cicely Rudder'
    'Lorraine Galban'
    'Trang Lenart'
    'Patrica Quirk'
    'Zackary Dedios'
    'Ursula Kennerly'
    'Shameka Flick'
    'President Loh'
  ]

  # Bottom Right: Latitude : 38.980296 | Longitude : -76.933479
  # Bottom Left: Latitude : 38.982297 | Longitude : -76.957941
  # Top Left: Latitude : 38.999109 | Longitude : -76.956053
  # Top Right: Latitude : 39.003778 | Longitude : -76.932278
  randGPS = () ->
    max = 1 # allow for repeated random coordinates

    # Calculate random GPS coordinates within campus
    leftLat = 38.994052
    rightLat = 38.981376
    bottomLng = -76.936569
    topLng = -76.950603
    skew = 1000000
    randLat = []
    randLng = []
    _.times max, ->
      randLat.push _.random(leftLat * skew, rightLat * skew) / skew
    _.times max, ->
      randLng.push _.random(bottomLng * skew, topLng * skew) / skew
    # Save in object to return
    randCoordinates =
      Lat: randLat
      Lng: randLng
    randCoordinates

  # Insert database of bikes if no data for today
  console.log 'Started creating DailyBikeData data schema'
  if DailyBikeData.find().count() is 0
    i = 1
    while i <= 50
      # create template for each DailyBikeData data stored
      Position = []
      randomNow = NaN
      blank = {}
      countTime = 0
      while countTime < 30
        # For 60 minutes in an hour
        randomNow = now - (10000000 * Math.random())
        namePoint = Math.round((randNames.length - 1) * Math.random())
        # console.log('randNames = ' + randNames);
        if Math.round(0.75 * Math.random()) is 0
          if Math.round(1.1 * Math.random()) is 0
            RandTag = 'Reserved'
          else
            RandTag = 'Available'
        else
          RandTag = 'RepairInProgress'
        blank =
          Tag: RandTag
          Rider: randNames[namePoint]
          Timestamp: randomNow
          Coordinates: randGPS()
        # console.log('name = ' + blank.User);
        Position.push blank
        countTime++
      DailyBikeData.insert
        Bike: i
        Day: today
        # simplified version
        Tag: RandTag
        Coordinates: Position[0].Coordinates
        Positions: Position
      i++
  console.log 'Done creating DailyBikeData data schema'



# Init
CreateDailyBikeData()