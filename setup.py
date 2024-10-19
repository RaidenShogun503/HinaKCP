from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from Cython.Build import cythonize  # Thêm import này để sử dụng Cython

extensions = [
    Extension(
        "kcp.extension",  # Tên mô-đun mở rộng
        sources=["kcp/extension.pyx", "kcp/ikcp.c"],  # Danh sách tệp nguồn
    )
]

setup(
    name='kcp',
    version='0.1',
    packages=['kcp'],
    install_requires=[
        'Cython',  # Cần có Cython để biên dịch .pyx
        # Các phụ thuộc khác nếu cần
    ],
    ext_modules=cythonize(extensions),  # Sử dụng cythonize để biên dịch mở rộng
    cmdclass={
        'build_ext': build_ext,  # Sử dụng build_ext đã được import
    },
)
