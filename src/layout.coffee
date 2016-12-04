defaultID = "Kyle King's Portfolio"

startJuxtapose = (id = null) ->
  microfluidics = document.getElementById('bead-bed')
  console.log('microfluidics')
  console.log(microfluidics)
  console.log(id)
  if (microfluidics != null || id == 'microfluidics')
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

  extensions = document.getElementById('web-clock')
  if (extensions != null || id == 'extensions')
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
  $('.cd-panel').removeClass 'is-visible'
  $('body').removeClass 'noscroll'
  # Remove tool tip as well
  $('.cd-panel-tooltip').removeClass 'visible'
  $('.tooltip-arrow-right').removeClass 'visible'
  homeURL = window.location.protocol + "//" + window.location.host + '/'
  console.log('homeURL')
  console.log(homeURL)
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


$( document ).ready(->
  if (window.location.pathname == '/')
    console.log('Already on home page!')
  else
    # Otherwise update the website to show the panel:
    document.title = getIDFromURL()
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'

  startJuxtapose()

  # # TODO: Used to open up panel right away for shared links:
  # # Useful for overcoming back button issue in flow.coffee
  # Template.layout.onRendered ->
  #   if Session.equals("NewVisitor", false)
  #     console.log 'Prevent open panel from running on route change'
  #   else
  #     console.log 'attempting to open panel'
  #     $('#cd-panel-toggle').addClass 'is-visible'
  #     # console.log $('.cd-panel').attr 'id'
  #     $('body').addClass 'noscroll'
  #   Session.set "NewVisitor", false
  #   console.log 'Set session to false'

  # Open up slide in panel on card click
  $( ".card-container" ).click (event) ->
    console.log 'Clicked .card-container'
    id = event.currentTarget.id
    if id
      createFullURL(id)
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      console.error('No known id to act upon...')

  # Close the panel on click
  $( ".cd-panel" ).click (event) ->
    console.log 'Clicked .cd-panel'
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      closePanel()

  # Tell user of esc button functionality:
  $( ".cd-panel-close" ).mouseover (event) ->
    # Show the tool tip on hover:
    $('.cd-panel-tooltip').addClass 'visible'
    $('.tooltip-arrow-right').addClass 'visible'
    # Remove tool tip on timeout:
    setTimeout (->
      $('.cd-panel-tooltip').removeClass 'visible'
      $('.tooltip-arrow-right').removeClass 'visible'
    ), 2000
)


document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'ESC key pressed!'
    closePanel()
