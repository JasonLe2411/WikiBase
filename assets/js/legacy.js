/*! Wiki.js - wiki.js.org - Licensed under AGPL */
(this.webpackJsonp=this.webpackJsonp||[]).push([["legacy"],{"./client/index-legacy.js":function(e,s,n){n("./client/scss/legacy.scss"),n("./client/scss/fonts/default.scss"),window.WIKI=null},"./client/scss/fonts/default.scss":function(e,s,n){var t=n("./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js"),o=n("./node_modules/mini-css-extract-plugin/dist/loader.js!./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/src/index.js!./node_modules/sass-loader/dist/cjs.js?!./node_modules/sass-resources-loader/lib/loader.js?!./client/scss/fonts/default.scss");"string"==typeof(o=o.__esModule?o.default:o)&&(o=[[e.i,o,""]]);var r={insert:"head",singleton:!1};t(o,r);e.exports=o.locals||{}},"./client/scss/legacy.scss":function(e,s,n){var t=n("./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js"),o=n("./node_modules/mini-css-extract-plugin/dist/loader.js!./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/src/index.js!./node_modules/sass-loader/dist/cjs.js?!./node_modules/sass-resources-loader/lib/loader.js?!./client/scss/legacy.scss");"string"==typeof(o=o.__esModule?o.default:o)&&(o=[[e.i,o,""]]);var r={insert:"head",singleton:!1};t(o,r);e.exports=o.locals||{}},"./node_modules/mini-css-extract-plugin/dist/loader.js!./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/src/index.js!./node_modules/sass-loader/dist/cjs.js?!./node_modules/sass-resources-loader/lib/loader.js?!./client/scss/fonts/default.scss":function(e,s,n){},"./node_modules/mini-css-extract-plugin/dist/loader.js!./node_modules/css-loader/dist/cjs.js!./node_modules/postcss-loader/src/index.js!./node_modules/sass-loader/dist/cjs.js?!./node_modules/sass-resources-loader/lib/loader.js?!./client/scss/legacy.scss":function(e,s,n){},"./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":function(e,s,n){"use strict";var t,o=function(){return void 0===t&&(t=Boolean(window&&document&&document.all&&!window.atob)),t},r=function(){var e={};return function(s){if(void 0===e[s]){var n=document.querySelector(s);if(window.HTMLIFrameElement&&n instanceof window.HTMLIFrameElement)try{n=n.contentDocument.head}catch(e){n=null}e[s]=n}return e[s]}}(),i=[];function d(e){for(var s=-1,n=0;n<i.length;n++)if(i[n].identifier===e){s=n;break}return s}function l(e,s){for(var n={},t=[],o=0;o<e.length;o++){var r=e[o],l=s.base?r[0]+s.base:r[0],a=n[l]||0,c="".concat(l," ").concat(a);n[l]=a+1;var u=d(c),f={css:r[1],media:r[2],sourceMap:r[3]};-1!==u?(i[u].references++,i[u].updater(f)):i.push({identifier:c,updater:v(f,s),references:1}),t.push(c)}return t}function a(e){var s=document.createElement("style"),t=e.attributes||{};if(void 0===t.nonce){var o=n.nc;o&&(t.nonce=o)}if(Object.keys(t).forEach((function(e){s.setAttribute(e,t[e])})),"function"==typeof e.insert)e.insert(s);else{var i=r(e.insert||"head");if(!i)throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");i.appendChild(s)}return s}var c,u=(c=[],function(e,s){return c[e]=s,c.filter(Boolean).join("\n")});function f(e,s,n,t){var o=n?"":t.media?"@media ".concat(t.media," {").concat(t.css,"}"):t.css;if(e.styleSheet)e.styleSheet.cssText=u(s,o);else{var r=document.createTextNode(o),i=e.childNodes;i[s]&&e.removeChild(i[s]),i.length?e.insertBefore(r,i[s]):e.appendChild(r)}}function m(e,s,n){var t=n.css,o=n.media,r=n.sourceMap;if(o?e.setAttribute("media",o):e.removeAttribute("media"),r&&"undefined"!=typeof btoa&&(t+="\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(r))))," */")),e.styleSheet)e.styleSheet.cssText=t;else{for(;e.firstChild;)e.removeChild(e.firstChild);e.appendChild(document.createTextNode(t))}}var p=null,j=0;function v(e,s){var n,t,o;if(s.singleton){var r=j++;n=p||(p=a(s)),t=f.bind(null,n,r,!1),o=f.bind(null,n,r,!0)}else n=a(s),t=m.bind(null,n,s),o=function(){!function(e){if(null===e.parentNode)return!1;e.parentNode.removeChild(e)}(n)};return t(e),function(s){if(s){if(s.css===e.css&&s.media===e.media&&s.sourceMap===e.sourceMap)return;t(e=s)}else o()}}e.exports=function(e,s){(s=s||{}).singleton||"boolean"==typeof s.singleton||(s.singleton=o());var n=l(e=e||[],s);return function(e){if(e=e||[],"[object Array]"===Object.prototype.toString.call(e)){for(var t=0;t<n.length;t++){var o=d(n[t]);i[o].references--}for(var r=l(e,s),a=0;a<n.length;a++){var c=d(n[a]);0===i[c].references&&(i[c].updater(),i.splice(c,1))}n=r}}}}},[["./client/index-legacy.js","runtime"]]]);