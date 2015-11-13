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