$( document ).ready(->
  if (window.location.host == "macbook-pro.local:5757")
    $('.cd-panel').addClass 'is-visible'
    $('body').addClass 'noscroll'

  slider = new (juxtapose.JXSlider)('#bead-bed', [
    {
      src: '../public/imgs/Microfluidics/microfluidics-21.jpg'
      label: 'Prior to Heating'
    }
    {
      src: '../public/imgs/Microfluidics/microfluidics-22.jpg'
      label: 'After Heating'
    }
  ], {
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '60%'
    makeResponsive: true
  })

  slider = new (juxtapose.JXSlider)('#web-clock', [
    {
      src: '../public/imgs/Extensions/extension-before.jpg'
      label: 'Standard UI'
    }
    {
      src: '../public/imgs/Extensions/extension-after.jpg'
      label: 'With Chrome Extension'
    }
  ], {
    animate: true
    showLabels: true
    showCredits: false
    startingPosition: '50%'
    makeResponsive: true
  })
)


