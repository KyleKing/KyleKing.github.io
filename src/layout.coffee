startJuxtapose = () ->
  console.log(window.location.pathname)
  # console.log(window.location.pathname)

  # # if (window.location.host == "macbook-pro.local:5757")
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

createFullURL = (id) ->
  # Figure out the URL
  newURL = window.location.protocol + "//" + window.location.host + '/'
  fullURL = newURL + 'pages/' + id + '.html'
  # Replace the current HTML content with the content corresponding to the desired state
  targetContent = document.getElementById("Slide-In-Panel-Content")
  targetHeader = document.getElementById("Slide-In-Panel-Header")
  targetContent.innerHTML = ''
  targetHeader.innerHTML = ''
  $.get fullURL, (data) ->
    targetContent.appendChild $(data).find("#Slide-In-Panel-Content")[0]
    targetHeader.appendChild $(data).find("#Slide-In-Panel-Header")[0]

  #   # # Not Applicable: Alternate to append the objects:
  #   # # $(data).find('.post').appendTo '.post-list'
  #   # i = 0
  #   # results = ''
  #   # targetContent.innerHTML = ''
  #   # len = $(data).length
  #   # while i < len
  #   #   targetContent.appendChild $(data)[i]
  #   #   i++

  # Update the route, so a refresh opens the complete page
  document.title = id
  window.history.pushState({
    "html": 'response.html'
    "pageTitle": id
  }, "", fullURL)

  startJuxtapose()
  return fullURL


$( document ).ready(->
  if (window.location.host == "macbook-pro.local:5757")
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'

  startJuxtapose()

  # TODO: Used to open up panel right away for shared links:
  # Useful for overcoming back button issue in flow.coffee
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

  # Open up slide in panel
  $( ".card-container" ).click (event) ->
    console.log 'Clicked .card-container'
    id = event.currentTarget.id
    # console.log 'Test me on mobile...maybe touch event has different object?'
    # console.log event.originalEvent.path
    if id
      createFullURL(id)
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      # FIXME:NOT YET BUILT for mobile!
      # path = event.originalEvent.path
      # console.log path
      # foundIDs = []
      # _.each path, (element) ->
      #   id = $(element).attr 'id'
      #   if id
      #     console.log id
      #     foundIDs.push id
      # id = foundIDs[0]
      # if id
      #   # FIXME: window.location.href = createFullURL(id)
      #   $('.cd-panel').addClass 'is-visible'
      #   $('body').addClass 'noscroll'
      # else
      #   console.log 'Could not find ID: ' + foundIDs
      console.log 'FIXME: NOT YET BUILT for mobile!'

  $( "button" ).click (event) ->
    console.log 'Clicked button'

  # Close the lateral panel
  $( ".cd-panel" ).click (event) ->
    console.log 'Clicked .cd-panel'
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      $('.cd-panel').removeClass 'is-visible'
      $('body').removeClass 'noscroll'
      # Remove tool tip as well
      $('.cd-panel-tooltip').removeClass 'visible'
      $('.tooltip-arrow-right').removeClass 'visible'
      event.preventDefault()

  # Tell user of esc button functionality:
  $( ".cd-panel-close" ).mouseover (event) ->
    console.log 'Clicked .cd-panel-close'
    $('.cd-panel-tooltip').addClass 'visible'
    $('.tooltip-arrow-right').addClass 'visible'
    setTimeout (->
      # Remove tool tip as well
      $('.cd-panel-tooltip').removeClass 'visible'
      $('.tooltip-arrow-right').removeClass 'visible'
    ), 2000
)


# Support Keyboard Shortcuts
document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'ESC key pressed!'

    # $('.cd-panel').addClass 'is-visible'
    # $('body').addClass 'noscroll'
    # $('.cd-panel-tooltip').addClass 'visible'
    # $('.tooltip-arrow-right').addClass 'visible'

    $('.cd-panel').removeClass 'is-visible'
    $('body').removeClass 'noscroll'
    # Remove tool tip as well
    $('.cd-panel-tooltip').removeClass 'visible'
    $('.tooltip-arrow-right').removeClass 'visible'
