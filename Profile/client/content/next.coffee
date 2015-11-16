Template.NEXT.onRendered ->
  slider = new (juxtapose.JXSlider)('#next-1', [
    {
      src: 'imgs/alumni_cup-4.jpg'
      label: '6:00 pm'
    }
    {
      src: 'imgs/alumni_cup-5.jpg'
      label: '11:59 pm'
    }
  ],
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '50%'
    makeResponsive: true)
