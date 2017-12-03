defaultID = "Kyle King's Portfolio"

startJuxtapose = (id = null) ->
  console.log 'Checking StartJuxtapose'

  if (document.getElementById('web-clock') != null || id == 'microfluidics')
    console.log 'Starting Juxtapose id: ' + id
    slider = new (juxtapose.JXSlider)('#bead-bed', [
      {
        src: '../public/imgs/Microfluidics/microfluidics-21.jpg'
        label: 'Prior to Heating'
      }
      {
        src: '../public/imgs/Microfluidics/microfluidics-22.jpg'
        label: 'After Heating'
      }
    ], {
      animate: true
      showLabels: true
      showCredits: false
      startingPosition: '60%'
      makeResponsive: true
    })

  if (document.getElementById('web-clock') != null || id == 'extensions')
    console.log 'Starting Juxtapose id: ' + id
    sliderTwo = new (juxtapose.JXSlider)('#web-clock', [
      {
        src: '../public/imgs/Extensions/extension-before.jpg'
        label: 'Standard UI'
      }
      {
        src: '../public/imgs/Extensions/extension-after.jpg'
        label: 'With Chrome Extension'
      }
    ], {
      animate: true
      showLabels: true
      showCredits: false
      startingPosition: '50%'
      makeResponsive: true
    })

closePanel = ->
  console.log 'Closing Panel'
  $('.cd-panel').removeClass 'is-visible'
  $('body').removeClass 'noscroll'
  # Remove tool tip as well
  $('.cd-panel-tooltip').removeClass 'visible'
  $('.tooltip-arrow-right').removeClass 'visible'
  homeURL = window.location.protocol + "//" + window.location.host + '/'
  document.title = defaultID
  window.history.pushState({
    "pageTitle": defaultID
  }, '', homeURL)

createFullURL = (id) ->
  # Figure out the URL
  newURL = window.location.protocol + "//" + window.location.host + '/'
  fullURL = newURL + 'pages/' + id + '.html'
  # Replace HTML content with the content of the desired state
  targetContent = document.getElementById("Slide-In-Panel-Content")
  targetHeader = document.getElementById("Slide-In-Panel-Header")
  targetContent.innerHTML = ''
  targetHeader.innerHTML = ''
  $.get fullURL, (data) ->
    targetContent.appendChild $(data).find("#Slide-In-Panel-Content")[0]
    targetHeader.appendChild $(data).find("#Slide-In-Panel-Header")[0]

  # Update the route, so a refresh opens the complete page
  document.title = id
  window.history.pushState({
    "html": 'response.html'
    "pageTitle": id
  }, "", fullURL)

  startJuxtapose(id)
  return fullURL

getIDFromURL = ->
  regex = /\/pages\/(.*)\.html/g
  m = regex.exec(window.location.pathname)
  if (m != null)
    id = m[1]
  else
    id = defaultID
  return id

showESCTooltip = ->
  # Show the tool tip on hover:
  $('.cd-panel-tooltip').addClass 'visible'
  $('.tooltip-arrow-right').addClass 'visible'
  # Remove tool tip on timeout:
  setTimeout (->
    $('.cd-panel-tooltip').removeClass 'visible'
    $('.tooltip-arrow-right').removeClass 'visible'
  ), 2000

$( document ).ready(->
  # Initialization
  if (window.location.pathname != '/')
    # If not on the home page, show the linked panel:
    document.title = getIDFromURL()
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'
    showESCTooltip()
  startJuxtapose()

  # Watch for card click to open corresponding panel
  $( ".card-container" ).click (event) ->
    id = event.currentTarget.id
    console.log 'Clicked .card-container for id: ' + id
    if id
      createFullURL(id)
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      console.error('No known id to act upon...')

  # Close the panel on click
  $( ".cd-panel" ).click (event) ->
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      closePanel()

  # Tell user of esc button functionality:
  $( ".cd-panel-header" ).mouseover (event) ->
    console.log 'Hovering on .cd-panel-close'
    showESCTooltip()
)

# Watch for ESC button press
document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'ESC key pressed!'
    closePanel()

# On Back Button, close panel
window.onpopstate = (e) ->
  if (e.state)
    console.log 'Back Event State: ' + JSON.stringify(e.state)
  closePanel()
