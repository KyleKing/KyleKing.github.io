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

Template.about.events
  'click .project-card': (event) ->
    # FlowRouter.go('/AdminCompilation/ManageMechanicNotes_Form/' + rowData._id)
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'