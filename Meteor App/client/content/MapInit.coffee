@IconLogic = (Tag) ->
  # Determine color of bike marker based on bike tag
  if Tag is 'Available'
    BikeIcon = window.Available
  else if Tag is 'RepairInProgress'
    BikeIcon = window.Damaged
  else if Tag is 'Reserved'
    BikeIcon = window.Reserved
  else if Tag is 'BikeRack'
    BikeIcon = window.BikeRack
  else
    BikeIcon = window.Reserved
  BikeIcon

@MapInit = (MapInitSettings) ->
  # Just to call for the bike variables and not an entire init
  if MapInitSettings.MapName != false
    # Create the Leaflet Map
    L.Icon.Default.imagePath = 'packages/bevanhunt_leaflet/images'
    window[MapInitSettings.MapName] = new (L.Map)( MapInitSettings.MapName, {
      center: MapInitSettings.Center
    })
    L.tileLayer.provider('OpenStreetMap.Mapnik').addTo window[MapInitSettings.MapName]
    window[MapInitSettings.MapName].spin false

    # Give user control over location
    window.LocateControl = L.control.locate(
      drawCircle: true
      follow: true
      setView: true
      keepCurrentZoomLevel: false
      remainActive: false
      markerClass: L.circleMarker).addTo window[MapInitSettings.MapName]

    # # Quickly load map (Doesn't seem to work reliably)
    # window[MapInitSettings.MapName].setView MapInitSettings.Center, 16

    # Automatically track user or center on UMD at arbitrary location
    if MapInitSettings.LocateUser
      # Start automatically
      window.LocateControl.start()
      window[MapInitSettings.MapName].on 'locationfound', (self) ->
        if MapInitSettings.PopupGuide
          console.log self
          # Create popup with user guide
          popup = L.popup()
          popup.setLatLng [self.latitude, self.longitude]
          popup.setContent MapInitSettings.PopupGuide
          popup.openOn window[MapInitSettings.MapName]
        Session.set "UserLocation": {lat: self.latitude, lng: self.longitude}
      window[MapInitSettings.MapName].on 'dragstart', window.LocateControl._stopFollowing, window.LocateControl
    else
      # Quickly load map
      window[MapInitSettings.MapName].setView MapInitSettings.Center, 16


  # Init Vars
  RackPositionMarkers = []
  RackOutlinePolygons = []


  # Unselected, but available
  window.Available = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'bicycle'
    markerColor: 'cadetblue'
    iconColor: 'white')
  # Damaged (InRepair) bike
  window.Damaged = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'bicycle'
    markerColor: 'darkred'
    iconColor: 'white')
  # Reserved
  window.Reserved = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'bicycle'
    markerColor: 'orange'
    iconColor: 'white')
  # Selected
  window.Selected = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'bicycle'
    markerColor: 'green'
    iconColor: 'white')
  # Redistributed
  window.Redistributed = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'bicycle'
    markerColor: 'purple'
    iconColor: 'white')
  # BikeRack
  window.BikeRack = L.AwesomeMarkers.icon(
    prefix: 'fa'
    icon: 'archive'
    markerColor: 'purple'
    iconColor: 'white')

@MapInitDestroyedFunction = ->
  window.MapObserveOuterLineHandle.stop()
  # Then clear  window[MapInitSettings.MapName] variable before loading a new map
  # console.log 'Deleting ' + window[MapInitSettings.MapName]
  # delete window[MapInitSettings.MapName]
  console.log 'Stopping LocateControl'
  # delete LocateControl
  window.LocateControl.stop()
