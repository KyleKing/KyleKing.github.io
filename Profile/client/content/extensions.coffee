Template.extensions.onRendered ->
  slider = new (juxtapose.JXSlider)('#web-clock', [
    {
      src: 'imgs/extension-before.png'
      label: 'Standard UI'
    }
    {
      src: 'imgs/extension-after.png'
      label: 'With Chrome Extension'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '50%'
    makeResponsive: true)