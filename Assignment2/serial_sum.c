#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <math.h>
#include <string.h>

#define SIZE 10000000
#define MAX_THREADS 128
#define NUM_TESTS 10

void generate_random(double *input, size_t size) {
    for (size_t i = 0; i < size; ++i) {
        input[i] = rand() / (double)(RAND_MAX);
    }
}

double serial_sum(double *x, size_t size) {
    double sum = 0.0;
    for (size_t i = 0; i < size; ++i) {
        sum += x[i];
    }
    return sum;
}

double omp_sum(double *x, size_t size) {
    double sum = 0.0;
    #pragma omp parallel for reduction(+:sum)
    for (size_t i = 0; i < size; ++i) {
        sum += x[i];
    }
    return sum;
}

double omp_critical_sum(double *x, size_t size) {
    double sum = 0.0;
    #pragma omp parallel for
    for (size_t i = 0; i < size; ++i) {
        #pragma omp critical
        sum += x[i];
    }
    return sum;
}

double omp_local_sum(double *x, size_t size) {
    double local_sum[MAX_THREADS] = {0};
    double sum = 0.0;
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        #pragma omp for
        for (size_t i = 0; i < size; ++i) {
            local_sum[id] += x[i];
        }
    }

    for (int i = 0; i < omp_get_max_threads(); ++i) {
        sum += local_sum[i];
    }
    return sum;
}

// Function to measure the performance
void measure_performance(double (*sum_function)(double*, size_t), double *array, size_t size, const char *name) {
    double times[NUM_TESTS];
    double sum = 0.0;
    for (int i = 0; i < NUM_TESTS; ++i) {
        double start_time = omp_get_wtime();
        sum = sum_function(array, size);
        double end_time = omp_get_wtime();
        times[i] = end_time - start_time;
    }

    // Calculate average and standard deviation
    double average_time = 0.0;
    for (int i = 0; i < NUM_TESTS; ++i) {
        average_time += times[i];
    }
    average_time /= NUM_TESTS;

    double std_dev = 0.0;
    for (int i = 0; i < NUM_TESTS; ++i) {
        std_dev += pow(times[i] - average_time, 2);
    }
    std_dev = sqrt(std_dev / NUM_TESTS);

    printf("%s: Average Time: %f seconds, Standard Deviation: %f seconds\n", name, average_time, std_dev);
}

int main() {
    double *array = (double *)malloc(SIZE * sizeof(double));
    if (array == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    generate_random(array, SIZE);

    printf("Performance Measurement:\n");
    measure_performance(serial_sum, array, SIZE, "Serial Sum");
    measure_performance(omp_sum, array, SIZE, "OMP Sum");
    measure_performance(omp_critical_sum, array, SIZE, "OMP Critical Sum");
    measure_performance(omp_local_sum, array, SIZE, "OMP Local Sum");

    free(array);
    return 0;
}