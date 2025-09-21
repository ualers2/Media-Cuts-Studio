import { EditionThemeOption, ShortifyOption, LegendsThemeOption, ChannelVideosResponse, TaskSchedulerProps, Account } from '@/lib/api';

export const weekdays = [
  { label: 'Monday', value: 'monday' },
  { label: 'Tuesday', value: 'tuesday' },
  { label: 'Wednesday', value: 'wednesday' },
  { label: 'Thursday', value: 'thursday' },
  { label: 'Friday', value: 'friday' },
  { label: 'Saturday', value: 'saturday' },
  { label: 'Sunday', value: 'sunday' },
];

export const slogans = [
"Media Cuts: O futuro da edição de conteúdo.",
"Transforme vídeos longos em cortes virais com a Curadoria IA.",
"A nossa IA corta e edita por você!",
"✂️ Pare de gastar horas na edição",
"Cada corte é meticulosamente selecionado pela nossa IA."
];
export const LegendsthemeOptions: LegendsThemeOption[] = [
{ 
    name: 'Revelation Effect - Tema Classico',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: '2',
    CaptionsColor: 'aqua',
    CaptionsFontName: 'Future',
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: '&HC0C0C0',
    CaptionsSecondaryColour: '&H8080',
    CaptionsOutlineColour: '&H0',
    CaptionsBackColour: '&H0',
    CaptionsBold: 1,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 3,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: '&HC8C8C8',
    CaptionsRevealEffectFinalColor: '&HDECF01',
    },
},
{
    name: 'Revelation Effect - Tema Noturno Minimalista',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "white",
    CaptionsFontName: "Arial",
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: "&HFFFFFF",
    CaptionsSecondaryColour: "&H8888FF",
    CaptionsOutlineColour: "&H000000",
    CaptionsBackColour: "&H80000000",
    CaptionsBold: 0,
    CaptionsItalic: 1,
    CaptionsUnderline: 0,
    CaptionsOutline: 2,
    CaptionsShadow: 0,
    CaptionsRevealEffectInitialColor: "&H000000&",
    CaptionsRevealEffectFinalColor: "&HFFFFFF&"
    },
},
{
    name: 'Revelation Effect - Tema Claro Elegante',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "black",
    CaptionsFontName: "Verdana",
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: "&H000000",
    CaptionsSecondaryColour: "&HAAAAAA",
    CaptionsOutlineColour: "&HFFFFFF",
    CaptionsBackColour: "&H80FFFFFF",
    CaptionsBold: 0,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 1,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: "&HFFFFFF&",
    CaptionsRevealEffectFinalColor: "&H000000&"
    },
},
{
    name: 'Revelation Effect - Tema Cinema Clássico',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "ivory",
    CaptionsFontName: "Georgia",
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: "&HEEEEE0",
    CaptionsSecondaryColour: "&H777760",
    CaptionsOutlineColour: "&H000000",
    CaptionsBackColour: "&H40000000",
    CaptionsBold: 1,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 3,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: "&H000000&",
    CaptionsRevealEffectFinalColor: "&HEEEEE0&"
    },
},
{
    name: 'Revelation Effect - Tema Neon Cyberpunk',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "cyan",
    CaptionsFontName: "Tahoma",
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: "&H00FFFF",
    CaptionsSecondaryColour: "&HFF00FF",
    CaptionsOutlineColour: "&H000020",
    CaptionsBackColour: "&H60000000",
    CaptionsBold: 1,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 4,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: "&H000020&",
    CaptionsRevealEffectFinalColor: "&H00FFFF&"
    },
},

{
    name: 'Revelation Effect - Tema Outono Rústico',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "saddlebrown",
    CaptionsFontName: "Palatino Linotype",
    CaptionsFontsize: 9,
    CaptionsPrimaryColour: "&H445522",
    CaptionsSecondaryColour: "&HCC8844",
    CaptionsOutlineColour: "&H000000",
    CaptionsBackColour: "&H60004433",
    CaptionsBold: 0,
    CaptionsItalic: 1,
    CaptionsUnderline: 0,
    CaptionsOutline: 2,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: "&H000000&",
    CaptionsRevealEffectFinalColor: "&HCC8844&"
    },
},

{
    name: 'Revelation Effect - Tema Marinho Calmaria',
    gif: '/gifs/Revelation Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: "2",
    CaptionsColor: "navy",
    CaptionsFontName: "Tahoma",
    CaptionsFontsize: 20,
    CaptionsPrimaryColour: "&H001144",
    CaptionsSecondaryColour: "&H88CCFF",
    CaptionsOutlineColour: "&H000000",
    CaptionsBackColour: "&H40001122",
    CaptionsBold: 0,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 1,
    CaptionsShadow: 1,
    CaptionsRevealEffectInitialColor: "&H001144&",
    CaptionsRevealEffectFinalColor: "&H88CCFF&"
    },
},



{
    name: 'Typewriter Effect - Tema Classico',
    gif: '/gifs/Typewriter Effect.gif', 
    settings: {
    SubtitleVerticalReference: '+20',
    SubtitleFontsize: '30',
    SubtitleColor: 'white',
    SubtitleAnimation: 'Slow Fade-Out',
    SubtitleEffects: 'Glow Effect',
    SubtitleFontName: 'Future',
    CaptionsAlignment: '2',
    CaptionsColor: 'white',
    CaptionsFontName: 'Arial',
    CaptionsFontsize: 16,
    CaptionsPrimaryColour: '&HFFFFFF',
    CaptionsSecondaryColour: '&H000000',
    CaptionsOutlineColour: '&H000000',
    CaptionsBackColour: '&H000000',
    CaptionsBold: 0,
    CaptionsItalic: 0,
    CaptionsUnderline: 0,
    CaptionsOutline: 1,
    CaptionsShadow: 0,
    CaptionsRevealEffectInitialColor: '&HFFFFFF',
    CaptionsRevealEffectFinalColor: '&HFFFFFF',
    },
},
// você pode adicionar quantos temas quiser seguindo o mesmo padrão
];
export const EditionthemeOptions: EditionThemeOption[] = [
{
    name: 'Thumbnail Vertical Fusion'
},
{
    name: 'AI Vertical Fusion'
}
];
export const ShortifyOptions: ShortifyOption[] = [
{
    name: 'Studio-Startup'
},
{
    name: 'Studio-Mini'
}
// ,    
// {
//   name: 'Studio-Deep-Think'
// },

];