'use strict';

/* App Module */

var fuisceApp = angular.module('fuisceApp', [
  'ngRoute',
  'fuisceControllers',
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
