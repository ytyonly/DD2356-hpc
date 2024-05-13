
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <mpi.h>

#define SEED     921
#define NUM_ITER 1000000000

int main(int argc, char* argv[])
{
    int rank, num_ranks;

    int count = 0;
    double x, y, z, pi;
    double start_time, end_time;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_ranks);
    
    int iter_per_rank = NUM_ITER / num_ranks;
    int local_count = 0;
    
    // Important: Multiply SEED by "rank" when you introduce MPI!
    srand(SEED * rank); 

    // Start measuring time
    start_time = MPI_Wtime();

    // Calculate PI following a Monte Carlo method
    for (int iter = 0; iter < iter_per_rank; iter++)
    {
        // Generate random (X,Y) points
        x = (double)random() / (double)RAND_MAX;
        y = (double)random() / (double)RAND_MAX;
        z = sqrt((x*x) + (y*y));
        
        // Check if point is in unit circle
        if (z <= 1.0)
        {
            local_count++;
        }
    }
    
    MPI_Reduce(&local_count, &count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    // Estimate Pi and display the result
    if (rank == 0) {
        pi = ((double)count / (double)NUM_ITER) * 4.0;
        end_time = MPI_Wtime();
        printf("The result is %f\n", pi);
        printf("Execution time: %f seconds\n", end_time - start_time);
    }
    
    MPI_Finalize();

    return 0;
}

