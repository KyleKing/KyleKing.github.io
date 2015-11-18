# Open up slide in panel
Template.about.events
  'click .card-container': (event) ->
    id = event.toElement.id
    console.log 'Test me on mobile...maybe touch event has different object?'
    console.log event.originalEvent.path
    if id
      FlowRouter.go('/' + id)
      # Now done with router event
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      path = event.originalEvent.path
      console.log path
      foundIDs = []
      _.each path, (element) ->
        id = $(element).attr 'id'
        if id
          console.log id
          foundIDs.push id
      id = foundIDs[0]
      if id
        FlowRouter.go('/' + id)
        # Now done with router event
        $('.cd-panel').addClass 'is-visible'
        $('body').addClass 'noscroll'
      else
        console.log 'Could not find ID: ' + foundIDs

  'click button': (event) ->
    # console.log event
    # if event.toElement is undefined
    #   console.log 'toElement is undefined'
    id = event.currentTarget.id
    # console.log 'Test me on mobile...maybe touch event has different object?'
    # console.log event.originalEvent.path
    if id
      FlowRouter.go('/' + id)
      # Now done with router event
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      path = event.originalEvent.path
      # console.log path
      foundIDs = []
      _.each path, (element) ->
        id = $(element).attr 'id'
        if id
          # console.log id
          foundIDs.push id
      id = foundIDs[0]
      if id
        FlowRouter.go('/' + id)
        # Now done with router event
        $('.cd-panel').addClass 'is-visible'
        $('body').addClass 'noscroll'
      else
        console.log 'Could not find ID: ' + foundIDs



# Close panel either with esc key or with click event
Template.layout.events
  #close the lateral panel
  'click .cd-panel': (event) ->
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      $('.cd-panel').removeClass 'is-visible'
      $('body').removeClass 'noscroll'
      # Remove tool tip as well
      $('.cd-panel-tooltip').removeClass 'visible'
      $('.tooltip-arrow-right').removeClass 'visible'
      event.preventDefault()
  # Tell user of esc button functionality
  # dblclick, focus, blur, mouseover, and change
  'mouseover .cd-panel-close': (event) ->
    $('.cd-panel-tooltip').addClass 'visible'
    $('.tooltip-arrow-right').addClass 'visible'
    setTimeout (->
      # Remove tool tip as well
      $('.cd-panel-tooltip').removeClass 'visible'
      $('.tooltip-arrow-right').removeClass 'visible'
    ), 2000


document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'Escape key was pressed'
    $('.cd-panel').removeClass 'is-visible'
    $('body').removeClass 'noscroll'
    # Remove tool tip as well
    $('.cd-panel-tooltip').removeClass 'visible'
    $('.tooltip-arrow-right').removeClass 'visible'