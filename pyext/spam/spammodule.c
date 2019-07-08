#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
spam_system(PyObject *self, PyObject *args) {
	const char *command = NULL;
	int sts = 0;

	if (!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	sts = system(command);
	return PyLong_FromLong(sts);
}
        
