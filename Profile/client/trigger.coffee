

# Open up slide in panel
Template.about.events
  'click .description-container button': (event) ->
    id = event.toElement.id
    if id
      FlowRouter.go('/' + id)
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      console.log 'Could not find ID: ' + id

# Close panel either with esc key or with click event
Template.layout.events
  #close the lateral panel
  'click .cd-panel': (event) ->
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      $('.cd-panel').removeClass 'is-visible'
      $('body').removeClass 'noscroll'
      event.preventDefault()
  # Tell user of esc button functionality
  # dblclick, focus, blur, mouseover, and change
  'mouseover .cd-panel-close': (event) ->
    console.log 'hover'
    $('.cd-panel-tooltip').addClass 'visible'
    # data-tooltip="Or press ESC" data-tooltip-direction="w"

document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'Escape key was pressed'
    $('.cd-panel').removeClass 'is-visible'
    $('body').removeClass 'noscroll'