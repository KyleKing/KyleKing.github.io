import {
  defineConfig,
  presetAttributify,
  presetIcons,
  presetUno,
} from 'unocss'

export default defineConfig({
  rules: [
    ['img-rounded', { 'object-fit': 'cover', 'border-radius': '50%' }]
  ],
  shortcuts: {
    'social-icon': 'text-inherit op30'
  },
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons({
      scale: 1.2,
      cdn: 'https://esm.sh/'
    }),
  ]
})
