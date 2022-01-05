/*
Copyright 2019 The Kubernetes Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
// Code generated by client-gen. DO NOT EDIT.

package v1beta1

import (
	v1beta1 "github.com/kubeflow/katib/pkg/apis/controller/trials/v1beta1"
	scheme "github.com/kubeflow/katib/pkg/client/controller/clientset/versioned/scheme"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	rest "k8s.io/client-go/rest"
)

// TrialsGetter has a method to return a TrialInterface.
// A group's client should implement this interface.
type TrialsGetter interface {
	Trials(namespace string) TrialInterface
}

// TrialInterface has methods to work with Trial resources.
type TrialInterface interface {
	Create(*v1beta1.Trial) (*v1beta1.Trial, error)
	Update(*v1beta1.Trial) (*v1beta1.Trial, error)
	UpdateStatus(*v1beta1.Trial) (*v1beta1.Trial, error)
	Delete(name string, options *v1.DeleteOptions) error
	DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error
	Get(name string, options v1.GetOptions) (*v1beta1.Trial, error)
	List(opts v1.ListOptions) (*v1beta1.TrialList, error)
	Watch(opts v1.ListOptions) (watch.Interface, error)
	Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1beta1.Trial, err error)
	TrialExpansion
}

// trials implements TrialInterface
type trials struct {
	client rest.Interface
	ns     string
}

// newTrials returns a Trials
func newTrials(c *TrialV1beta1Client, namespace string) *trials {
	return &trials{
		client: c.RESTClient(),
		ns:     namespace,
	}
}

// Get takes name of the trial, and returns the corresponding trial object, and an error if there is any.
func (c *trials) Get(name string, options v1.GetOptions) (result *v1beta1.Trial, err error) {
	result = &v1beta1.Trial{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("trials").
		Name(name).
		VersionedParams(&options, scheme.ParameterCodec).
		Do().
		Into(result)
	return
}

// List takes label and field selectors, and returns the list of Trials that match those selectors.
func (c *trials) List(opts v1.ListOptions) (result *v1beta1.TrialList, err error) {
	result = &v1beta1.TrialList{}
	err = c.client.Get().
		Namespace(c.ns).
		Resource("trials").
		VersionedParams(&opts, scheme.ParameterCodec).
		Do().
		Into(result)
	return
}

// Watch returns a watch.Interface that watches the requested trials.
func (c *trials) Watch(opts v1.ListOptions) (watch.Interface, error) {
	opts.Watch = true
	return c.client.Get().
		Namespace(c.ns).
		Resource("trials").
		VersionedParams(&opts, scheme.ParameterCodec).
		Watch()
}

// Create takes the representation of a trial and creates it.  Returns the server's representation of the trial, and an error, if there is any.
func (c *trials) Create(trial *v1beta1.Trial) (result *v1beta1.Trial, err error) {
	result = &v1beta1.Trial{}
	err = c.client.Post().
		Namespace(c.ns).
		Resource("trials").
		Body(trial).
		Do().
		Into(result)
	return
}

// Update takes the representation of a trial and updates it. Returns the server's representation of the trial, and an error, if there is any.
func (c *trials) Update(trial *v1beta1.Trial) (result *v1beta1.Trial, err error) {
	result = &v1beta1.Trial{}
	err = c.client.Put().
		Namespace(c.ns).
		Resource("trials").
		Name(trial.Name).
		Body(trial).
		Do().
		Into(result)
	return
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().

func (c *trials) UpdateStatus(trial *v1beta1.Trial) (result *v1beta1.Trial, err error) {
	result = &v1beta1.Trial{}
	err = c.client.Put().
		Namespace(c.ns).
		Resource("trials").
		Name(trial.Name).
		SubResource("status").
		Body(trial).
		Do().
		Into(result)
	return
}

// Delete takes name of the trial and deletes it. Returns an error if one occurs.
func (c *trials) Delete(name string, options *v1.DeleteOptions) error {
	return c.client.Delete().
		Namespace(c.ns).
		Resource("trials").
		Name(name).
		Body(options).
		Do().
		Error()
}

// DeleteCollection deletes a collection of objects.
func (c *trials) DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error {
	return c.client.Delete().
		Namespace(c.ns).
		Resource("trials").
		VersionedParams(&listOptions, scheme.ParameterCodec).
		Body(options).
		Do().
		Error()
}

// Patch applies the patch and returns the patched trial.
func (c *trials) Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1beta1.Trial, err error) {
	result = &v1beta1.Trial{}
	err = c.client.Patch(pt).
		Namespace(c.ns).
		Resource("trials").
		SubResource(subresources...).
		Name(name).
		Body(data).
		Do().
		Into(result)
	return
}
