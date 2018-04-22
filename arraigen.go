package proto

//go:generate protoc -I . arrai.proto --go_out=plugins=grpc:.
//go:generate python2 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. arrai.proto
