# coding: utf-8

"""
    Katib

    Swagger description for Katib  # noqa: E501

    OpenAPI spec version: v1alpha3-0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.katib.models.v1alpha3_metrics_collector_spec import V1alpha3MetricsCollectorSpec  # noqa: F401,E501
from kubeflow.katib.models.v1alpha3_objective_spec import V1alpha3ObjectiveSpec  # noqa: F401,E501
from kubeflow.katib.models.v1alpha3_parameter_assignment import V1alpha3ParameterAssignment  # noqa: F401,E501


class V1alpha3TrialSpec(object):
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
        'metrics_collector': 'V1alpha3MetricsCollectorSpec',
        'objective': 'V1alpha3ObjectiveSpec',
        'parameter_assignments': 'list[V1alpha3ParameterAssignment]',
        'retain_run': 'bool',
        'run_spec': 'str'
    }

    attribute_map = {
        'metrics_collector': 'metricsCollector',
        'objective': 'objective',
        'parameter_assignments': 'parameterAssignments',
        'retain_run': 'retainRun',
        'run_spec': 'runSpec'
    }

    def __init__(self, metrics_collector=None, objective=None, parameter_assignments=None, retain_run=None, run_spec=None):  # noqa: E501
        """V1alpha3TrialSpec - a model defined in Swagger"""  # noqa: E501

        self._metrics_collector = None
        self._objective = None
        self._parameter_assignments = None
        self._retain_run = None
        self._run_spec = None
        self.discriminator = None

        if metrics_collector is not None:
            self.metrics_collector = metrics_collector
        if objective is not None:
            self.objective = objective
        self.parameter_assignments = parameter_assignments
        if retain_run is not None:
            self.retain_run = retain_run
        if run_spec is not None:
            self.run_spec = run_spec

    @property
    def metrics_collector(self):
        """Gets the metrics_collector of this V1alpha3TrialSpec.  # noqa: E501

        Describes how metrics will be collected  # noqa: E501

        :return: The metrics_collector of this V1alpha3TrialSpec.  # noqa: E501
        :rtype: V1alpha3MetricsCollectorSpec
        """
        return self._metrics_collector

    @metrics_collector.setter
    def metrics_collector(self, metrics_collector):
        """Sets the metrics_collector of this V1alpha3TrialSpec.

        Describes how metrics will be collected  # noqa: E501

        :param metrics_collector: The metrics_collector of this V1alpha3TrialSpec.  # noqa: E501
        :type: V1alpha3MetricsCollectorSpec
        """

        self._metrics_collector = metrics_collector

    @property
    def objective(self):
        """Gets the objective of this V1alpha3TrialSpec.  # noqa: E501

        Describes the objective of the experiment.  # noqa: E501

        :return: The objective of this V1alpha3TrialSpec.  # noqa: E501
        :rtype: V1alpha3ObjectiveSpec
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this V1alpha3TrialSpec.

        Describes the objective of the experiment.  # noqa: E501

        :param objective: The objective of this V1alpha3TrialSpec.  # noqa: E501
        :type: V1alpha3ObjectiveSpec
        """

        self._objective = objective

    @property
    def parameter_assignments(self):
        """Gets the parameter_assignments of this V1alpha3TrialSpec.  # noqa: E501

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :return: The parameter_assignments of this V1alpha3TrialSpec.  # noqa: E501
        :rtype: list[V1alpha3ParameterAssignment]
        """
        return self._parameter_assignments

    @parameter_assignments.setter
    def parameter_assignments(self, parameter_assignments):
        """Sets the parameter_assignments of this V1alpha3TrialSpec.

        Key-value pairs for hyperparameters and assignment values.  # noqa: E501

        :param parameter_assignments: The parameter_assignments of this V1alpha3TrialSpec.  # noqa: E501
        :type: list[V1alpha3ParameterAssignment]
        """
        if parameter_assignments is None:
            raise ValueError("Invalid value for `parameter_assignments`, must not be `None`")  # noqa: E501

        self._parameter_assignments = parameter_assignments

    @property
    def retain_run(self):
        """Gets the retain_run of this V1alpha3TrialSpec.  # noqa: E501

        Whether to retain the trial run object after completed.  # noqa: E501

        :return: The retain_run of this V1alpha3TrialSpec.  # noqa: E501
        :rtype: bool
        """
        return self._retain_run

    @retain_run.setter
    def retain_run(self, retain_run):
        """Sets the retain_run of this V1alpha3TrialSpec.

        Whether to retain the trial run object after completed.  # noqa: E501

        :param retain_run: The retain_run of this V1alpha3TrialSpec.  # noqa: E501
        :type: bool
        """

        self._retain_run = retain_run

    @property
    def run_spec(self):
        """Gets the run_spec of this V1alpha3TrialSpec.  # noqa: E501

        Raw text for the trial run spec. This can be any generic Kubernetes runtime object. The trial operator should create the resource as written, and let the corresponding resource controller (e.g. tf-operator) handle the rest.  # noqa: E501

        :return: The run_spec of this V1alpha3TrialSpec.  # noqa: E501
        :rtype: str
        """
        return self._run_spec

    @run_spec.setter
    def run_spec(self, run_spec):
        """Sets the run_spec of this V1alpha3TrialSpec.

        Raw text for the trial run spec. This can be any generic Kubernetes runtime object. The trial operator should create the resource as written, and let the corresponding resource controller (e.g. tf-operator) handle the rest.  # noqa: E501

        :param run_spec: The run_spec of this V1alpha3TrialSpec.  # noqa: E501
        :type: str
        """

        self._run_spec = run_spec

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
        if issubclass(V1alpha3TrialSpec, dict):
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
        if not isinstance(other, V1alpha3TrialSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
