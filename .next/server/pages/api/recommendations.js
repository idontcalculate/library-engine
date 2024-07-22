"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/api/recommendations";
exports.ids = ["pages/api/recommendations"];
exports.modules = {

/***/ "dotenv":
/*!*************************!*\
  !*** external "dotenv" ***!
  \*************************/
/***/ ((module) => {

module.exports = require("dotenv");

/***/ }),

/***/ "fastembed":
/*!****************************!*\
  !*** external "fastembed" ***!
  \****************************/
/***/ ((module) => {

module.exports = require("fastembed");

/***/ }),

/***/ "next/dist/compiled/next-server/pages-api.runtime.dev.js":
/*!**************************************************************************!*\
  !*** external "next/dist/compiled/next-server/pages-api.runtime.dev.js" ***!
  \**************************************************************************/
/***/ ((module) => {

module.exports = require("next/dist/compiled/next-server/pages-api.runtime.dev.js");

/***/ }),

/***/ "@qdrant/js-client-rest":
/*!*****************************************!*\
  !*** external "@qdrant/js-client-rest" ***!
  \*****************************************/
/***/ ((module) => {

module.exports = import("@qdrant/js-client-rest");;

/***/ }),

/***/ "(api)/./node_modules/next/dist/build/webpack/loaders/next-route-loader/index.js?kind=PAGES_API&page=%2Fapi%2Frecommendations&preferredRegion=&absolutePagePath=.%2Fpages%2Fapi%2Frecommendations.js&middlewareConfigBase64=e30%3D!":
/*!************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-route-loader/index.js?kind=PAGES_API&page=%2Fapi%2Frecommendations&preferredRegion=&absolutePagePath=.%2Fpages%2Fapi%2Frecommendations.js&middlewareConfigBase64=e30%3D! ***!
  \************************************************************************************************************************************************************************************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.a(module, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {\n__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   config: () => (/* binding */ config),\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__),\n/* harmony export */   routeModule: () => (/* binding */ routeModule)\n/* harmony export */ });\n/* harmony import */ var next_dist_server_future_route_modules_pages_api_module_compiled__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/dist/server/future/route-modules/pages-api/module.compiled */ \"(api)/./node_modules/next/dist/server/future/route-modules/pages-api/module.compiled.js\");\n/* harmony import */ var next_dist_server_future_route_modules_pages_api_module_compiled__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_future_route_modules_pages_api_module_compiled__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_dist_server_future_route_kind__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/dist/server/future/route-kind */ \"(api)/./node_modules/next/dist/server/future/route-kind.js\");\n/* harmony import */ var next_dist_build_templates_helpers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/dist/build/templates/helpers */ \"(api)/./node_modules/next/dist/build/templates/helpers.js\");\n/* harmony import */ var _pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./pages/api/recommendations.js */ \"(api)/./pages/api/recommendations.js\");\nvar __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([_pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__]);\n_pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__ = (__webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__)[0];\n\n\n\n// Import the userland code.\n\n// Re-export the handler (should be the default export).\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ((0,next_dist_build_templates_helpers__WEBPACK_IMPORTED_MODULE_2__.hoist)(_pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__, \"default\"));\n// Re-export config.\nconst config = (0,next_dist_build_templates_helpers__WEBPACK_IMPORTED_MODULE_2__.hoist)(_pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__, \"config\");\n// Create and export the route module that will be consumed.\nconst routeModule = new next_dist_server_future_route_modules_pages_api_module_compiled__WEBPACK_IMPORTED_MODULE_0__.PagesAPIRouteModule({\n    definition: {\n        kind: next_dist_server_future_route_kind__WEBPACK_IMPORTED_MODULE_1__.RouteKind.PAGES_API,\n        page: \"/api/recommendations\",\n        pathname: \"/api/recommendations\",\n        // The following aren't used in production.\n        bundlePath: \"\",\n        filename: \"\"\n    },\n    userland: _pages_api_recommendations_js__WEBPACK_IMPORTED_MODULE_3__\n});\n\n//# sourceMappingURL=pages-api.js.map\n__webpack_async_result__();\n} catch(e) { __webpack_async_result__(e); } });//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9ub2RlX21vZHVsZXMvbmV4dC9kaXN0L2J1aWxkL3dlYnBhY2svbG9hZGVycy9uZXh0LXJvdXRlLWxvYWRlci9pbmRleC5qcz9raW5kPVBBR0VTX0FQSSZwYWdlPSUyRmFwaSUyRnJlY29tbWVuZGF0aW9ucyZwcmVmZXJyZWRSZWdpb249JmFic29sdXRlUGFnZVBhdGg9LiUyRnBhZ2VzJTJGYXBpJTJGcmVjb21tZW5kYXRpb25zLmpzJm1pZGRsZXdhcmVDb25maWdCYXNlNjQ9ZTMwJTNEISIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7OztBQUFzRztBQUN2QztBQUNMO0FBQzFEO0FBQzJEO0FBQzNEO0FBQ0EsaUVBQWUsd0VBQUssQ0FBQywwREFBUSxZQUFZLEVBQUM7QUFDMUM7QUFDTyxlQUFlLHdFQUFLLENBQUMsMERBQVE7QUFDcEM7QUFDTyx3QkFBd0IsZ0hBQW1CO0FBQ2xEO0FBQ0EsY0FBYyx5RUFBUztBQUN2QjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsS0FBSztBQUNMLFlBQVk7QUFDWixDQUFDOztBQUVELHFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vbGlicmFyeS1lbmdpbmUvP2QzYjgiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgUGFnZXNBUElSb3V0ZU1vZHVsZSB9IGZyb20gXCJuZXh0L2Rpc3Qvc2VydmVyL2Z1dHVyZS9yb3V0ZS1tb2R1bGVzL3BhZ2VzLWFwaS9tb2R1bGUuY29tcGlsZWRcIjtcbmltcG9ydCB7IFJvdXRlS2luZCB9IGZyb20gXCJuZXh0L2Rpc3Qvc2VydmVyL2Z1dHVyZS9yb3V0ZS1raW5kXCI7XG5pbXBvcnQgeyBob2lzdCB9IGZyb20gXCJuZXh0L2Rpc3QvYnVpbGQvdGVtcGxhdGVzL2hlbHBlcnNcIjtcbi8vIEltcG9ydCB0aGUgdXNlcmxhbmQgY29kZS5cbmltcG9ydCAqIGFzIHVzZXJsYW5kIGZyb20gXCIuL3BhZ2VzL2FwaS9yZWNvbW1lbmRhdGlvbnMuanNcIjtcbi8vIFJlLWV4cG9ydCB0aGUgaGFuZGxlciAoc2hvdWxkIGJlIHRoZSBkZWZhdWx0IGV4cG9ydCkuXG5leHBvcnQgZGVmYXVsdCBob2lzdCh1c2VybGFuZCwgXCJkZWZhdWx0XCIpO1xuLy8gUmUtZXhwb3J0IGNvbmZpZy5cbmV4cG9ydCBjb25zdCBjb25maWcgPSBob2lzdCh1c2VybGFuZCwgXCJjb25maWdcIik7XG4vLyBDcmVhdGUgYW5kIGV4cG9ydCB0aGUgcm91dGUgbW9kdWxlIHRoYXQgd2lsbCBiZSBjb25zdW1lZC5cbmV4cG9ydCBjb25zdCByb3V0ZU1vZHVsZSA9IG5ldyBQYWdlc0FQSVJvdXRlTW9kdWxlKHtcbiAgICBkZWZpbml0aW9uOiB7XG4gICAgICAgIGtpbmQ6IFJvdXRlS2luZC5QQUdFU19BUEksXG4gICAgICAgIHBhZ2U6IFwiL2FwaS9yZWNvbW1lbmRhdGlvbnNcIixcbiAgICAgICAgcGF0aG5hbWU6IFwiL2FwaS9yZWNvbW1lbmRhdGlvbnNcIixcbiAgICAgICAgLy8gVGhlIGZvbGxvd2luZyBhcmVuJ3QgdXNlZCBpbiBwcm9kdWN0aW9uLlxuICAgICAgICBidW5kbGVQYXRoOiBcIlwiLFxuICAgICAgICBmaWxlbmFtZTogXCJcIlxuICAgIH0sXG4gICAgdXNlcmxhbmRcbn0pO1xuXG4vLyMgc291cmNlTWFwcGluZ1VSTD1wYWdlcy1hcGkuanMubWFwIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(api)/./node_modules/next/dist/build/webpack/loaders/next-route-loader/index.js?kind=PAGES_API&page=%2Fapi%2Frecommendations&preferredRegion=&absolutePagePath=.%2Fpages%2Fapi%2Frecommendations.js&middlewareConfigBase64=e30%3D!\n");

/***/ }),

/***/ "(api)/./pages/api/recommendations.js":
/*!**************************************!*\
  !*** ./pages/api/recommendations.js ***!
  \**************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.a(module, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {\n__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ handler)\n/* harmony export */ });\n/* harmony import */ var _qdrant_js_client_rest__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @qdrant/js-client-rest */ \"@qdrant/js-client-rest\");\n/* harmony import */ var dotenv__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! dotenv */ \"dotenv\");\n/* harmony import */ var dotenv__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(dotenv__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var fastembed__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! fastembed */ \"fastembed\");\n/* harmony import */ var fastembed__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(fastembed__WEBPACK_IMPORTED_MODULE_2__);\nvar __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([_qdrant_js_client_rest__WEBPACK_IMPORTED_MODULE_0__]);\n_qdrant_js_client_rest__WEBPACK_IMPORTED_MODULE_0__ = (__webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__)[0];\n\n\n\ndotenv__WEBPACK_IMPORTED_MODULE_1___default().config();\nconst client = new _qdrant_js_client_rest__WEBPACK_IMPORTED_MODULE_0__.Client({\n    apiKey: process.env.QDRANT_API_KEY,\n    url: process.env.QDRANT_URL\n});\nasync function handler(req, res) {\n    if (req.method !== \"POST\") {\n        res.setHeader(\"Allow\", [\n            \"POST\"\n        ]);\n        return res.status(405).end(`Method ${req.method} Not Allowed`);\n    }\n    const { bookTitle, category } = req.body;\n    if (!bookTitle || !category) {\n        return res.status(400).json({\n            error: \"Book title and category are required\"\n        });\n    }\n    try {\n        const queryVector = await fastembed__WEBPACK_IMPORTED_MODULE_2___default().embed([\n            `${bookTitle} ${category}`\n        ]);\n        const response = await client.search({\n            collection_name: \"your_collection_name\",\n            vector: queryVector[0],\n            top: 5\n        });\n        const recommendations = response.result.map((result)=>result.payload.title);\n        return res.status(200).json({\n            recommendations\n        });\n    } catch (error) {\n        console.error(\"Error querying Qdrant:\", error);\n        return res.status(500).json({\n            error: \"Internal Server Error\"\n        });\n    }\n}\n\n__webpack_async_result__();\n} catch(e) { __webpack_async_result__(e); } });//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwaSkvLi9wYWdlcy9hcGkvcmVjb21tZW5kYXRpb25zLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7OztBQUFnRDtBQUNwQjtBQUNNO0FBRWxDQyxvREFBYTtBQUViLE1BQU1HLFNBQVMsSUFBSUosMERBQU1BLENBQUM7SUFDeEJLLFFBQVFDLFFBQVFDLEdBQUcsQ0FBQ0MsY0FBYztJQUNsQ0MsS0FBS0gsUUFBUUMsR0FBRyxDQUFDRyxVQUFVO0FBQzdCO0FBRWUsZUFBZUMsUUFBUUMsR0FBRyxFQUFFQyxHQUFHO0lBQzVDLElBQUlELElBQUlFLE1BQU0sS0FBSyxRQUFRO1FBQ3pCRCxJQUFJRSxTQUFTLENBQUMsU0FBUztZQUFDO1NBQU87UUFDL0IsT0FBT0YsSUFBSUcsTUFBTSxDQUFDLEtBQUtDLEdBQUcsQ0FBQyxDQUFDLE9BQU8sRUFBRUwsSUFBSUUsTUFBTSxDQUFDLFlBQVksQ0FBQztJQUMvRDtJQUVBLE1BQU0sRUFBRUksU0FBUyxFQUFFQyxRQUFRLEVBQUUsR0FBR1AsSUFBSVEsSUFBSTtJQUV4QyxJQUFJLENBQUNGLGFBQWEsQ0FBQ0MsVUFBVTtRQUMzQixPQUFPTixJQUFJRyxNQUFNLENBQUMsS0FBS0ssSUFBSSxDQUFDO1lBQUVDLE9BQU87UUFBdUM7SUFDOUU7SUFFQSxJQUFJO1FBQ0YsTUFBTUMsY0FBYyxNQUFNckIsc0RBQWUsQ0FBQztZQUFDLENBQUMsRUFBRWdCLFVBQVUsQ0FBQyxFQUFFQyxTQUFTLENBQUM7U0FBQztRQUV0RSxNQUFNTSxXQUFXLE1BQU1yQixPQUFPc0IsTUFBTSxDQUFDO1lBQ25DQyxpQkFBaUI7WUFDakJDLFFBQVFMLFdBQVcsQ0FBQyxFQUFFO1lBQ3RCTSxLQUFLO1FBQ1A7UUFFQSxNQUFNQyxrQkFBa0JMLFNBQVNNLE1BQU0sQ0FBQ0MsR0FBRyxDQUFDLENBQUNELFNBQVdBLE9BQU9FLE9BQU8sQ0FBQ0MsS0FBSztRQUU1RSxPQUFPckIsSUFBSUcsTUFBTSxDQUFDLEtBQUtLLElBQUksQ0FBQztZQUFFUztRQUFnQjtJQUNoRCxFQUFFLE9BQU9SLE9BQU87UUFDZGEsUUFBUWIsS0FBSyxDQUFDLDBCQUEwQkE7UUFDeEMsT0FBT1QsSUFBSUcsTUFBTSxDQUFDLEtBQUtLLElBQUksQ0FBQztZQUFFQyxPQUFPO1FBQXdCO0lBQy9EO0FBQ0YiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9saWJyYXJ5LWVuZ2luZS8uL3BhZ2VzL2FwaS9yZWNvbW1lbmRhdGlvbnMuanM/OGMzMiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBDbGllbnQgfSBmcm9tICdAcWRyYW50L2pzLWNsaWVudC1yZXN0JztcbmltcG9ydCBkb3RlbnYgZnJvbSAnZG90ZW52JztcbmltcG9ydCBGYXN0RW1iZWQgZnJvbSAnZmFzdGVtYmVkJztcblxuZG90ZW52LmNvbmZpZygpO1xuXG5jb25zdCBjbGllbnQgPSBuZXcgQ2xpZW50KHtcbiAgYXBpS2V5OiBwcm9jZXNzLmVudi5RRFJBTlRfQVBJX0tFWSxcbiAgdXJsOiBwcm9jZXNzLmVudi5RRFJBTlRfVVJMLFxufSk7XG5cbmV4cG9ydCBkZWZhdWx0IGFzeW5jIGZ1bmN0aW9uIGhhbmRsZXIocmVxLCByZXMpIHtcbiAgaWYgKHJlcS5tZXRob2QgIT09ICdQT1NUJykge1xuICAgIHJlcy5zZXRIZWFkZXIoJ0FsbG93JywgWydQT1NUJ10pO1xuICAgIHJldHVybiByZXMuc3RhdHVzKDQwNSkuZW5kKGBNZXRob2QgJHtyZXEubWV0aG9kfSBOb3QgQWxsb3dlZGApO1xuICB9XG5cbiAgY29uc3QgeyBib29rVGl0bGUsIGNhdGVnb3J5IH0gPSByZXEuYm9keTtcblxuICBpZiAoIWJvb2tUaXRsZSB8fCAhY2F0ZWdvcnkpIHtcbiAgICByZXR1cm4gcmVzLnN0YXR1cyg0MDApLmpzb24oeyBlcnJvcjogJ0Jvb2sgdGl0bGUgYW5kIGNhdGVnb3J5IGFyZSByZXF1aXJlZCcgfSk7XG4gIH1cblxuICB0cnkge1xuICAgIGNvbnN0IHF1ZXJ5VmVjdG9yID0gYXdhaXQgRmFzdEVtYmVkLmVtYmVkKFtgJHtib29rVGl0bGV9ICR7Y2F0ZWdvcnl9YF0pO1xuICAgIFxuICAgIGNvbnN0IHJlc3BvbnNlID0gYXdhaXQgY2xpZW50LnNlYXJjaCh7XG4gICAgICBjb2xsZWN0aW9uX25hbWU6ICd5b3VyX2NvbGxlY3Rpb25fbmFtZScsXG4gICAgICB2ZWN0b3I6IHF1ZXJ5VmVjdG9yWzBdLFxuICAgICAgdG9wOiA1LCAvLyBudW1iZXIgb2YgcmVjb21tZW5kYXRpb25zIHRvIHJldHJpZXZlXG4gICAgfSk7XG5cbiAgICBjb25zdCByZWNvbW1lbmRhdGlvbnMgPSByZXNwb25zZS5yZXN1bHQubWFwKChyZXN1bHQpID0+IHJlc3VsdC5wYXlsb2FkLnRpdGxlKTtcblxuICAgIHJldHVybiByZXMuc3RhdHVzKDIwMCkuanNvbih7IHJlY29tbWVuZGF0aW9ucyB9KTtcbiAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICBjb25zb2xlLmVycm9yKCdFcnJvciBxdWVyeWluZyBRZHJhbnQ6JywgZXJyb3IpO1xuICAgIHJldHVybiByZXMuc3RhdHVzKDUwMCkuanNvbih7IGVycm9yOiAnSW50ZXJuYWwgU2VydmVyIEVycm9yJyB9KTtcbiAgfVxufVxuIl0sIm5hbWVzIjpbIkNsaWVudCIsImRvdGVudiIsIkZhc3RFbWJlZCIsImNvbmZpZyIsImNsaWVudCIsImFwaUtleSIsInByb2Nlc3MiLCJlbnYiLCJRRFJBTlRfQVBJX0tFWSIsInVybCIsIlFEUkFOVF9VUkwiLCJoYW5kbGVyIiwicmVxIiwicmVzIiwibWV0aG9kIiwic2V0SGVhZGVyIiwic3RhdHVzIiwiZW5kIiwiYm9va1RpdGxlIiwiY2F0ZWdvcnkiLCJib2R5IiwianNvbiIsImVycm9yIiwicXVlcnlWZWN0b3IiLCJlbWJlZCIsInJlc3BvbnNlIiwic2VhcmNoIiwiY29sbGVjdGlvbl9uYW1lIiwidmVjdG9yIiwidG9wIiwicmVjb21tZW5kYXRpb25zIiwicmVzdWx0IiwibWFwIiwicGF5bG9hZCIsInRpdGxlIiwiY29uc29sZSJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(api)/./pages/api/recommendations.js\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../webpack-api-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, ["vendor-chunks/next"], () => (__webpack_exec__("(api)/./node_modules/next/dist/build/webpack/loaders/next-route-loader/index.js?kind=PAGES_API&page=%2Fapi%2Frecommendations&preferredRegion=&absolutePagePath=.%2Fpages%2Fapi%2Frecommendations.js&middlewareConfigBase64=e30%3D!")));
module.exports = __webpack_exports__;

})();