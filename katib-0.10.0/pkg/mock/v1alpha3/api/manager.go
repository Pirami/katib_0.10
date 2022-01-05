// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/kubeflow/katib/pkg/apis/manager/v1alpha3 (interfaces: ManagerClient)

// Package mock is a generated GoMock package.
package mock

import (
	context "context"
	gomock "github.com/golang/mock/gomock"
	api_v1_alpha3 "github.com/kubeflow/katib/pkg/apis/manager/v1alpha3"
	grpc "google.golang.org/grpc"
	reflect "reflect"
)

// MockManagerClient is a mock of ManagerClient interface.
type MockManagerClient struct {
	ctrl     *gomock.Controller
	recorder *MockManagerClientMockRecorder
}

// MockManagerClientMockRecorder is the mock recorder for MockManagerClient.
type MockManagerClientMockRecorder struct {
	mock *MockManagerClient
}

// NewMockManagerClient creates a new mock instance.
func NewMockManagerClient(ctrl *gomock.Controller) *MockManagerClient {
	mock := &MockManagerClient{ctrl: ctrl}
	mock.recorder = &MockManagerClientMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use.
func (m *MockManagerClient) EXPECT() *MockManagerClientMockRecorder {
	return m.recorder
}

// DeleteObservationLog mocks base method.
func (m *MockManagerClient) DeleteObservationLog(arg0 context.Context, arg1 *api_v1_alpha3.DeleteObservationLogRequest, arg2 ...grpc.CallOption) (*api_v1_alpha3.DeleteObservationLogReply, error) {
	m.ctrl.T.Helper()
	varargs := []interface{}{arg0, arg1}
	for _, a := range arg2 {
		varargs = append(varargs, a)
	}
	ret := m.ctrl.Call(m, "DeleteObservationLog", varargs...)
	ret0, _ := ret[0].(*api_v1_alpha3.DeleteObservationLogReply)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// DeleteObservationLog indicates an expected call of DeleteObservationLog.
func (mr *MockManagerClientMockRecorder) DeleteObservationLog(arg0, arg1 interface{}, arg2 ...interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	varargs := append([]interface{}{arg0, arg1}, arg2...)
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "DeleteObservationLog", reflect.TypeOf((*MockManagerClient)(nil).DeleteObservationLog), varargs...)
}

// GetObservationLog mocks base method.
func (m *MockManagerClient) GetObservationLog(arg0 context.Context, arg1 *api_v1_alpha3.GetObservationLogRequest, arg2 ...grpc.CallOption) (*api_v1_alpha3.GetObservationLogReply, error) {
	m.ctrl.T.Helper()
	varargs := []interface{}{arg0, arg1}
	for _, a := range arg2 {
		varargs = append(varargs, a)
	}
	ret := m.ctrl.Call(m, "GetObservationLog", varargs...)
	ret0, _ := ret[0].(*api_v1_alpha3.GetObservationLogReply)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// GetObservationLog indicates an expected call of GetObservationLog.
func (mr *MockManagerClientMockRecorder) GetObservationLog(arg0, arg1 interface{}, arg2 ...interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	varargs := append([]interface{}{arg0, arg1}, arg2...)
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "GetObservationLog", reflect.TypeOf((*MockManagerClient)(nil).GetObservationLog), varargs...)
}

// ReportObservationLog mocks base method.
func (m *MockManagerClient) ReportObservationLog(arg0 context.Context, arg1 *api_v1_alpha3.ReportObservationLogRequest, arg2 ...grpc.CallOption) (*api_v1_alpha3.ReportObservationLogReply, error) {
	m.ctrl.T.Helper()
	varargs := []interface{}{arg0, arg1}
	for _, a := range arg2 {
		varargs = append(varargs, a)
	}
	ret := m.ctrl.Call(m, "ReportObservationLog", varargs...)
	ret0, _ := ret[0].(*api_v1_alpha3.ReportObservationLogReply)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// ReportObservationLog indicates an expected call of ReportObservationLog.
func (mr *MockManagerClientMockRecorder) ReportObservationLog(arg0, arg1 interface{}, arg2 ...interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	varargs := append([]interface{}{arg0, arg1}, arg2...)
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "ReportObservationLog", reflect.TypeOf((*MockManagerClient)(nil).ReportObservationLog), varargs...)
}
