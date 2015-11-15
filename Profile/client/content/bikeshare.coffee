Template.bikeshare.onRendered ->
  slider = new (juxtapose.JXSlider)('#bikeshare-1', [
    {
      src: 'imgs/bikeshare-05.jpg'
      label: 'Smartlock Design'
    }
    {
      src: 'imgs/bikeshare-07.jpg'
      label: 'Concept Sketch'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '70%'
    makeResponsive: true)


Template.bikeshare.rendered = ->
  @subscribe("DailyBikeDataPub")

  # Call MapInit function from s_Helpers
  MapInit
    MapName: 'DemoMap'
    LocateUser: false
    DrawOutline: false
    Center: [38.987701, -76.940989]
    ShowClosestBikes: false
    FullScreenButton: false
    PopupGuide: "I'm a bike!"
    ShowBikeRacksMarkerToggle: false

  # Inspiration: http://meteorcapture.com/how-to-create-a-reactive-google-map/
  # and leaflet specific: http://asynchrotron.com/blog/2013/12/28/realtime-maps-with-meteor-and-leaflet-part-2/
  MapMarkers = []


  [today, now] = CurrentDay()
  window.MapObserveHandle = DailyBikeData.find({}).observe
    added: (bike) ->
      latlng = [Number(bike.Coordinates.Lat), bike.Coordinates.Lng]
      BikeIcon = IconLogic(bike.Tag)
      MapMarkers[bike._id] = L.marker(latlng,
        title: bike.Bike
        opacity: 0.75
        icon: BikeIcon).on("click", (e) ->
          # Important Vars
          [today, now] = CurrentDay()
          SelectedBike = e.target.options.title
          Session.set
            'selectedBike': SelectedBike
            'available': false
          # Find bike info
          coords = DailyBikeData.findOne({Bike: SelectedBike}).Coordinates
          latlng = [Number(coords.Lat), Number(coords.Lng)]
          window.DemoMap.panTo latlng, 18
          ).addTo(window.DemoMap)

    changed: (bike, oldBike) ->
      latlng = [Number(bike.Coordinates.Lat), Number(bike.Coordinates.Lng)]
      MapMarkers[bike._id].setLatLng(latlng).update()
      if bike.Tag is 'Reserved'
        MapMarkers[bike._id].setIcon window.Reserved
        console.log 'Changed to reserved icon for # ' + bike.Bike
       else if bike.Tag is 'RepairInProgress'
        MapMarkers[bike._id].setIcon window.Damaged
        console.log 'Changed to damaged icon for # ' + bike.Bike
      else if bike.Tag is "Available"
        MapMarkers[bike._id].setIcon window.Available
        console.log 'Changed to gray icon color for # ' + bike.Bike
      else
        console.log bike.Tag

    removed: (oldBike) ->
      # Remove the marker from the map
      window.DemoMap.removeLayer MapMarkers[oldBike._id]
      # Remove the reference to this marker instance
      delete MapMarkers[oldBike._id]


Template.bikeshare.events
  # 'click #DeleteRFID': ->
  #   console.log @_id + ' will be deleted'
  #   # Only able to delete by id
  #   RFIDdata.remove @_id
  'click #DeleteOldBikes': ->
    # Not allowed to call mongo remove query from client, so call method
    Meteor.call 'DeleteOldBikes'