FlowRouter.notFound = action: ->
  BlazeLayout.render 'layout', {
    body: '404'
  }

FlowRouter.route '/',
  name: 'about',
  action: ->
    BlazeLayout.render 'layout', {
      body: 'about'
      Slide_In_Panel_Title: 'Slide_In_Panel_Placeholder_Title'
      Slide_In_Panel_Content: 'Slide_In_Panel_Placeholder'
    }

IDs = [
  'microfluidics'
  'bikeshare'
  'side-project'
  'Canon'
  'extensions'
  '3D_printing'
  'alumni_cup'
  'class_projects'
  'microduino'
  'NEXT'
]

_.each IDs, (ID) ->
  route = '/' + ID
  FlowRouter.route route,
    name: ID,
    action: ->
      BlazeLayout.render 'layout', {
        body: 'about'
        Slide_In_Panel_Title: ID + '_title'
        Slide_In_Panel_Content: ID
      }


# Scroll to the top of every page
ScrollToTop = ->
  # Gotta love a mature programming language: http://stackoverflow.com/questions/9316415/the-same-old-issue-scrolltop0-not-working-in-chrome-safari
  # $(window).scrollTop 0
  # Not so fast: http://stackoverflow.com/a/5580456/3219667
  $('#Slide-In-Panel-Content').animate { scrollTop: 0 }, 'slow'

FlowRouter.triggers.enter ScrollToTop, except: [
  'about'
]

# Make sure panel is open when go to specific link (i.e. someone shares a link)
OpenPanel = ->
  Template.layout.rendered = ->
    # console.log 'attempting to open panel'
    $('#cd-panel-toggle').addClass 'is-visible'
    # console.log $('.cd-panel').attr 'id'
    $('body').addClass 'noscroll'

FlowRouter.triggers.enter OpenPanel, except: [
  'about'
]