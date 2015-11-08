FlowRouter.route '/',
  name: 'about',
  action: ->
    BlazeLayout.render 'layout', {
      body: 'about'
      Slide_In_Panel_Title: 'Slide_In_Panel_Placeholder_Title'
      Slide_In_Panel_Content: 'Slide_In_Panel_Placeholder'
    }

# FlowRouter.route '/AdminCompilation/ManageBike/:IDofSelectedRow',
#   name: 'AdminCompilation/ManageBike',
#   action: (params, queryParams) ->
#     BlazeLayout.render 'layout', {
#       body: 'AdminCompilation'
#       Slide_In_Panel_Title: 'ManageBike_Title'
#       Slide_In_Panel_Content: 'ManageBike'
#     }