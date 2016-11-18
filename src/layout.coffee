createFullURL = (id) ->
  newURL = window.location.protocol + "//" + window.location.host + '/'
  fullURL = newURL + 'pages/' + id + '.html'
  document.title = id
  window.history.pushState({
    "html": 'response.html'
    "pageTitle": id
  }, "", fullURL)
  return fullURL

$( document ).ready(->
  console.log 'ready!'

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
      console.log 'NOT YET BUILT'

  $( "button" ).click (event) ->
    console.log 'Clicked button'
    # # console.log event
    # # if event.toElement is undefined
    # #   console.log 'toElement is undefined'
    # id = event.currentTarget.id
    # # console.log 'Test me on mobile...maybe touch event has different object?'
    # # console.log event.originalEvent.path
    # if id
    #   # FIXME: FlowRouter.go('/' + id)
    #   # Now done with router event
    #   $('.cd-panel').addClass 'is-visible'
    #   $('body').addClass 'noscroll'
    # else
    #   path = event.originalEvent.path
    #   # console.log path
    #   foundIDs = []
    #   _.each path, (element) ->
    #     id = $(element).attr 'id'
    #     if id
    #       # console.log id
    #       foundIDs.push id
    #   id = foundIDs[0]
    #   if id
    #     # FIXME: FlowRouter.go('/' + id)
    #     # Now done with router event
    #     $('.cd-panel').addClass 'is-visible'
    #     $('body').addClass 'noscroll'
    #   else
    #     console.log 'Could not find ID: ' + foundIDs



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
