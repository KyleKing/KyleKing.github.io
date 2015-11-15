Template.bikeshare.rendered = ->
  # Create the Leaflet Map
  L.Icon.Default.imagePath = 'packages/bevanhunt_leaflet/images'
  map = new (L.Map)('DemoMap', center: new (L.LatLng)(38.987701, -76.940989))
  L.tileLayer.provider('OpenStreetMap.Mapnik').addTo map
  map.spin false
  markers = []
  # DailyBikeData.find({}).observe
  #   added: (bike) ->
  #     latlng = [
  #       bike.Positions.lat
  #       bike.Positions.lng
  #     ]
  #     marker = L.marker(latlng,
  #       title: '#' + bike.Bike + ' is ' + bike.Tag
  #       opacity: 0.5).addTo(map)
  #     # marker.bindPopup("#" + bike.Bike + " is " + bike.Tag);
  #     # Store this marker instance within the markers object.
  #     markers[bike._id] = marker
  #     console.log markers[bike._id] + ' added to map on ADDED event'
  #     return
  #   changed: (bike, oldDocument) ->
  #     latlng = [
  #       bike.Positions.lat
  #       bike.Positions.lng
  #     ]
  #     markers[bike._id].setLatLng(latlng).update()
  #     console.log markers[bike._id] + ' changed on map on CHANGED event'
  #     return
  #   removed: (oldBike) ->
  #     console.log oldBike
  #     # Remove the marker from the map
  #     map.removeLayer markers[oldBike._id]
  #     # Remove the reference to this marker instance
  #     delete markers[oldBike._id]
  #     console.log markers[oldBike._id] + ' removed from map on REMOVED event'
  #     return
  # bottomLng = -76.936569
  # topLng = -76.950603
  # leftLat = 38.994052
  # rightLat = 38.981376
  # polygon = L.polygon([
  #   [
  #     rightLat
  #     bottomLng
  #   ]
  #   [
  #     rightLat
  #     topLng
  #   ]
  #   [
  #     leftLat
  #     topLng
  #   ]
  #   [
  #     leftLat
  #     bottomLng
  #   ]
  # ]).addTo(map)
  # // Zoom to user location
  # map.locate({ setView: true })
  map.setView new (L.LatLng)(38.987701, -76.940989), 13
  # Notes for using included MarkCluster Package
  # var markers = new L.MarkerClusterGroup();
  # markers.addLayer(new L.Marker([51.5, -0.09]));
  # map.addLayer(markers);


# Template.bikeshare.onRendered ->
#   slider = new (juxtapose.JXSlider)('#bikeshare-1', [
#     {
#       src: 'imgs/bikeshare-05.jpg'
#       label: 'Smartlock Design'
#     }
#     {
#       src: 'imgs/bikeshare-07.jpg'
#       label: 'Concept Sketch'
#     }
#   ],
#     animate: true
#     showLabels: true
#     showCredits: false
#     startingPosition: '70%'
#     makeResponsive: true)


# Template.bikeshare.rendered = ->
#   @subscribe("DailyBikeDataPub")

#   # Call MapInit function from s_Helpers
#   MapInit
#     MapName: 'DemoMap'
#     LocateUser: false
#     DrawOutline: false
#     Center: [38.987701, -76.940989]
#     ShowClosestBikes: false
#     FullScreenButton: false
#     PopupGuide: "I'm a bike!"
#     ShowBikeRacksMarkerToggle: false

#   # # Inspiration: http://meteorcapture.com/how-to-create-a-reactive-google-map/
#   # # and leaflet specific: http://asynchrotron.com/blog/2013/12/28/realtime-maps-with-meteor-and-leaflet-part-2/
#   # MapMarkers = []
#   # # Session.set
#   # #   "selectedBike": false
#   # #   "available": true

#   # [today, now] = CurrentDay()
#   # window.MapObserveHandle = DailyBikeData.find().observe
#   #   added: (bike) ->
#   #     latlng = bike.Coordinates
#   #     console.log latlng
#   #     BikeIcon = IconLogic(bike.Tag)
#   #     console.log BikeIcon
#   #     MapMarkers[bike._id] = L.marker(latlng,
#   #       title: bike.Bike
#   #       opacity: 0.75
#   #       icon: BikeIcon).on("click", (e) ->
#   #         # Important Vars
#   #         [today, now] = CurrentDay()
#   #         SelectedBike = e.target.options.title
#   #         Session.set
#   #           'selectedBike': SelectedBike
#   #           'available': false
#   #         # Find bike info
#   #         coords = DailyBikeData.findOne({Bike: SelectedBike}).Coordinates
#   #         window.DemoMap.panTo coords, 18
#   #         ).addTo(window.DemoMap)

#   # #   changed: (bike, oldBike) ->
#   # #     if oldBike.Tag is bike.Tag
#   # #       latlng = bike.Coordinates
#   # #       MapMarkers[bike._id].setLatLng(latlng).update()
#   # #     else if bike.Tag is Meteor.userId()
#   # #       MapMarkers[bike._id].setIcon window.Reserved
#   # #       console.log 'Changed to green icon color for # ' + bike.Bike
#   # #     else if bike.Tag is "Available"
#   # #       MapMarkers[bike._id].setIcon window.Available
#   # #       console.log 'Changed to gray icon color for # ' + bike.Bike

#   # #   removed: (oldBike) ->
#   # #     if oldBike.Tag isnt Meteor.userId() and Session.get 'available'
#   # #       # If removed bike is currently selected bike...
#   # #       if Session.get("selectedBike") is oldBike.Bike
#   # #         # Updated reserve bike text
#   # #         Session.set "available": false
#   # #         # And alert user
#   # #         sAlert.error('Bike reserved by different user. Select new bike')
#   # #     # Remove the marker from the map
#   # #     window.BikeMap.removeLayer MapMarkers[oldBike._id]
#   # #     # Remove the reference to this marker instance
#   # #     delete MapMarkers[oldBike._id]


#   # # # [today, now] = CurrentDay()
#   # # # window.MapObserveHandle = DailyBikeData.find().observe
#   # # #   added: (bike) ->
#   # # #     latlng = bike.Coordinates
#   # # #     BikeIcon = IconLogic(bike.Tag)
#   # # #     MapMarkers[bike._id] = L.marker(latlng,
#   # # #       title: bike.Bike
#   # # #       opacity: 0.75
#   # # #       icon: BikeIcon).on("click", (e) ->
#   # # #         # Important Vars
#   # # #         [today, now] = CurrentDay()
#   # # #         SelectedBike = e.target.options.title
#   # # #         Session.set
#   # # #           'selectedBike': SelectedBike
#   # # #           'available': false
#   # # #         # Find bike info
#   # # #         coords = DailyBikeData.findOne({Bike: SelectedBike, Day: today}).Coordinates
#   # # #         window.BikeMap.panTo coords, 18
#   # # #         # Reserve bike
#   # # #         if Meteor.userId()
#   # # #           Meteor.call 'UserReserveBike', Meteor.userId(), SelectedBike, (error, result) ->
#   # # #             # Inform user of results
#   # # #             if error
#   # # #               console.log error.reason
#   # # #             else
#   # # #               sAlert.success('Bike #' + SelectedBike + ' successfully reserved for the next FIVE minutes!')
#   # # #               if result is 1
#   # # #                 sAlert.warning('1 previously reserved bike was re-listed as Available')
#   # # #               else if result isnt 0
#   # # #                 sAlert.warning(result + ' previously reserved bikes were re-listed as Available')
#   # # #         else
#   # # #           sAlert.warning('You must sign in to reserve a bike')
#   # # #         ).addTo(window.BikeMap)

#   # # #   changed: (bike, oldBike) ->
#   # # #     if oldBike.Tag is bike.Tag
#   # # #       latlng = bike.Coordinates
#   # # #       MapMarkers[bike._id].setLatLng(latlng).update()
#   # # #       console.log MapMarkers[bike._id]._leaflet_id + ' changed on window.BikeMap on CHANGED event'
#   # # #     else if bike.Tag is Meteor.userId()
#   # # #       MapMarkers[bike._id].setIcon window.Reserved
#   # # #       console.log 'Changed to green icon color for # ' + bike.Bike
#   # # #     else if bike.Tag is "Available"
#   # # #       MapMarkers[bike._id].setIcon window.Available
#   # # #       console.log 'Changed to gray icon color for # ' + bike.Bike
#   # # #     else
#   # # #       console.log "changed, but not with this logic"

#   # # #   removed: (oldBike) ->
#   # # #     if oldBike.Tag isnt Meteor.userId() and Session.get 'available'
#   # # #       # If removed bike is currently selected bike...
#   # # #       if Session.get("selectedBike") is oldBike.Bike
#   # # #         # Updated reserve bike text
#   # # #         Session.set "available": false
#   # # #         # And alert user
#   # # #         sAlert.error('Bike reserved by different user. Select new bike')
#   # # #     # Remove the marker from the map
#   # # #     console.log MapMarkers[oldBike._id]._leaflet_id + ' removed from window.BikeMap on REMOVED event'
#   # # #     window.BikeMap.removeLayer MapMarkers[oldBike._id]
#   # # #     # Remove the reference to this marker instance
#   # # #     delete MapMarkers[oldBike._id]