Template.bikeshare.onRendered ->
  slider = new (juxtapose.JXSlider)('#foo', [
    {
      src: 'imgs/bikeshare-3.jpg'
      label: '2009'
      credit: 'Image Credit'
    }
    {
      src: 'imgs/bikeshare-4.jpg'
      label: '2014'
      credit: 'Image Credit'
    }
  ],
    animate: true
    showLabels: true
    showCredits: true
    startingPosition: '50%'
    makeResponsive: true)