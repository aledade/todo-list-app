angular.module('todo.tasks', ['ui.sortable'])

.service('taskService', ['$http', function($http) {
  var ts = this;

  ts.getTasks = function() {
    return $http.get('/api/tasks');
  };
}])

.directive('manageTasks', ['taskService', function(taskService) {
  return {
    restrict:       'E',
    templateUrl:    function() {
      // Lazy "asset fingerprinting" - never cache the template
      return '/static/templates/manage-tasks.html?' + new Date().getTime();
    },
    link: function($scope) {
      taskService.getTasks().then(function(response) {
        $scope.tasks = response.data.tasks;
      });
    },
  };
}])

;
