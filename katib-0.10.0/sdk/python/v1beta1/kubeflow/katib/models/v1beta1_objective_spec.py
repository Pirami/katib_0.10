# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1beta1-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1beta1_metric_strategy import V1beta1MetricStrategy  # noqa: F401,E501


class V1beta1ObjectiveSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_metric_names': 'list[str]',
        'goal': 'float',
        'metric_strategies': 'list[V1beta1MetricStrategy]',
        'objective_metric_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_metric_names': 'additionalMetricNames',
        'goal': 'goal',
        'metric_strategies': 'metricStrategies',
        'objective_metric_name': 'objectiveMetricName',
        'type': 'type'
    }

    def __init__(self, additional_metric_names=None, goal=None, metric_strategies=None, objective_metric_name=None, type=None):  # noqa: E501
        """V1beta1ObjectiveSpec - a model defined in Swagger"""  # noqa: E501

        self._additional_metric_names = None
        self._goal = None
        self._metric_strategies = None
        self._objective_metric_name = None
        self._type = None
        self.discriminator = None

        if additional_metric_names is not None:
            self.additional_metric_names = additional_metric_names
        if goal is not None:
            self.goal = goal
        if metric_strategies is not None:
            self.metric_strategies = metric_strategies
        if objective_metric_name is not None:
            self.objective_metric_name = objective_metric_name
        if type is not None:
            self.type = type

    @property
    def additional_metric_names(self):
        """Gets the additional_metric_names of this V1beta1ObjectiveSpec.  # noqa: E501

        AdditionalMetricNames represents metrics that should be collected from Trials. This can be empty if we only care about the objective metric. Note: If we adopt a push instead of pull mechanism, this can be omitted completely.  # noqa: E501

        :return: The additional_metric_names of this V1beta1ObjectiveSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_metric_names

    @additional_metric_names.setter
    def additional_metric_names(self, additional_metric_names):
        """Sets the additional_metric_names of this V1beta1ObjectiveSpec.

        AdditionalMetricNames represents metrics that should be collected from Trials. This can be empty if we only care about the objective metric. Note: If we adopt a push instead of pull mechanism, this can be omitted completely.  # noqa: E501

        :param additional_metric_names: The additional_metric_names of this V1beta1ObjectiveSpec.  # noqa: E501
        :type: list[str]
        """

        self._additional_metric_names = additional_metric_names

    @property
    def goal(self):
        """Gets the goal of this V1beta1ObjectiveSpec.  # noqa: E501

        Goal is the Experiment's objective goal that should be reached. In case of empty goal, Experiment is running until MaxTrialCount = TrialsSucceeded.  # noqa: E501

        :return: The goal of this V1beta1ObjectiveSpec.  # noqa: E501
        :rtype: float
        """
        return self._goal

    @goal.setter
    def goal(self, goal):
        """Sets the goal of this V1beta1ObjectiveSpec.

        Goal is the Experiment's objective goal that should be reached. In case of empty goal, Experiment is running until MaxTrialCount = TrialsSucceeded.  # noqa: E501

        :param goal: The goal of this V1beta1ObjectiveSpec.  # noqa: E501
        :type: float
        """

        self._goal = goal

    @property
    def metric_strategies(self):
        """Gets the metric_strategies of this V1beta1ObjectiveSpec.  # noqa: E501

        MetricStrategies defines various rules (min, max or latest) to extract metrics values. This field is allowed to missing, experiment defaulter (webhook) will fill it.  # noqa: E501

        :return: The metric_strategies of this V1beta1ObjectiveSpec.  # noqa: E501
        :rtype: list[V1beta1MetricStrategy]
        """
        return self._metric_strategies

    @metric_strategies.setter
    def metric_strategies(self, metric_strategies):
        """Sets the metric_strategies of this V1beta1ObjectiveSpec.

        MetricStrategies defines various rules (min, max or latest) to extract metrics values. This field is allowed to missing, experiment defaulter (webhook) will fill it.  # noqa: E501

        :param metric_strategies: The metric_strategies of this V1beta1ObjectiveSpec.  # noqa: E501
        :type: list[V1beta1MetricStrategy]
        """

        self._metric_strategies = metric_strategies

    @property
    def objective_metric_name(self):
        """Gets the objective_metric_name of this V1beta1ObjectiveSpec.  # noqa: E501

        ObjectiveMetricName represents primary Experiment's metric to optimize.  # noqa: E501

        :return: The objective_metric_name of this V1beta1ObjectiveSpec.  # noqa: E501
        :rtype: str
        """
        return self._objective_metric_name

    @objective_metric_name.setter
    def objective_metric_name(self, objective_metric_name):
        """Sets the objective_metric_name of this V1beta1ObjectiveSpec.

        ObjectiveMetricName represents primary Experiment's metric to optimize.  # noqa: E501

        :param objective_metric_name: The objective_metric_name of this V1beta1ObjectiveSpec.  # noqa: E501
        :type: str
        """

        self._objective_metric_name = objective_metric_name

    @property
    def type(self):
        """Gets the type of this V1beta1ObjectiveSpec.  # noqa: E501

        Type for Experiment optimization.  # noqa: E501

        :return: The type of this V1beta1ObjectiveSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta1ObjectiveSpec.

        Type for Experiment optimization.  # noqa: E501

        :param type: The type of this V1beta1ObjectiveSpec.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1beta1ObjectiveSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1ObjectiveSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
