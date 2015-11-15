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

  # Note: aspect ratio of 5:7 in portrait
  slider = new (juxtapose.JXSlider)('#Syring-heater', [
    {
      src: 'imgs/microfluidics-04.jpg'
      label: 'With insulation'
    }
    {
      src: 'imgs/microfluidics-03.jpg'
      label: 'Testing'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '60%'
    makeResponsive: true)