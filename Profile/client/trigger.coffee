# Legacy support for trigger button for panel

Template.layout.events
  #open the lateral panel
  'click .cd-btn': (event) ->
    event.preventDefault()
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'
    return
  #close the lateral panel
  'click .cd-panel': (event) ->
    if $(event.target).is('.cd-panel') or $(event.target).is('.cd-panel-close')
      $('.cd-panel').removeClass 'is-visible'
      $('body').removeClass 'noscroll'
      event.preventDefault()

document.onkeydown = (evt) ->
  evt = evt or window.event
  if evt.keyCode == 27
    console.log 'Escape key was pressed'
    $('.cd-panel').removeClass 'is-visible'
    $('body').removeClass 'noscroll'

Template.about.events
  'click .description-container button': (event) ->
    id = event.toElement.id
    if id
      FlowRouter.go('/' + id)
      $('.cd-panel').addClass 'is-visible'
      $('body').addClass 'noscroll'
    else
      console.log 'Could not find ID: ' + id