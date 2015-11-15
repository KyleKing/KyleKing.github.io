Template.microfluidics.onRendered ->
  slider = new (juxtapose.JXSlider)('#bead-bed', [
    {
      src: 'imgs/microfluidics-21.jpg'
      label: 'Prior to Heating'
    }
    {
      src: 'imgs/microfluidics-22.jpg'
      label: 'After Heating'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '75%%'
    makeResponsive: true)