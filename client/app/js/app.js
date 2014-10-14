'use strict';

/* App Module */

var fuisceApp = angular.module('fuisceApp', [
  'ngRoute',
  'phonecatAnimations',
  'fuisceControllers',
  // 'phonecatFilters',
  'fuisceServices',
  'angular-growl'
]);

fuisceApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/review/', {
        templateUrl: 'partials/review.html',
        controller: 'ReviewController'
      }).
      otherwise({
        redirectTo: '/review'
      });
  }]);
