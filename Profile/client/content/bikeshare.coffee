Template.bikeshare.onRendered ->
  slider = new (juxtapose.JXSlider)('#bikeshare-1', [
    {
      src: 'imgs/bikeshare-05.jpg'
      label: 'Smartlock Design'
    }
    {
      src: 'imgs/bikeshare-07.jpg'
      label: 'Concept Sketch'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '70%'
    makeResponsive: true)

  # slider = new (juxtapose.JXSlider)('#bikeshare-2', [
  #   {
  #     src: 'imgs/bikeshare-05.jpg'
  #     label: 'Smartlock Design'
  #   }
  #   {
  #     src: 'imgs/bikeshare-07.jpg'
  #     label: 'Concept Sketch'
  #   }
  # ],
  #   animate: true
  #   showLabels: true
  #   showCredits: false
  #   startingPosition: '70%'
  #   makeResponsive: true)