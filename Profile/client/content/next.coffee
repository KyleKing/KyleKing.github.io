Template.NEXT.onRendered ->
  slider = new (juxtapose.JXSlider)('#next-1', [
    {
      src: 'imgs/alumni_cup-4.jpg'
    }
    {
      src: 'imgs/alumni_cup-5.jpg'
    }
  ],
    animate: true
    showLabels: false
    showCredits: false
    startingPosition: '60%'
    makeResponsive: true)
