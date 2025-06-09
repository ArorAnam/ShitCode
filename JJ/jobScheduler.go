package main

import (
	"errors"
	"fmt"
	"sync"
)

// JOb represents a unit of work with an ID and input data
type Job struct {
	ID    int
	Input int
}

// result hold the outout of a processed job or an error
type Result struct {
	Job    Job
	Output int
	Err    error
}

func processJob(job Job) Result {
	if job.Input < 0 {
		return Result{job, 0, errors.New("Negative input not allowed !!")}
	}
	return Result{job, job.Input * 2, nil}
}

// worker process jobs from the jobs channel and sends results to the results channel.
func worker(id int, jobs <-chan Job, results chan<- Result, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		results <- processJob(job)
	}
}

// scheduler creates a worker pool and manages job distribution
func scheduler(jobs []Job, numWorkers int) (map[int]int, []error) {
	var wg sync.WaitGroup
	jobsChan := make(chan Job, len(jobs))
	resultsChan := make(chan Result, len(jobs))

	// Start workers
	wg.Add(numWorkers)
	for i := 0; i < numWorkers; i++ {
		go worker(i, jobsChan, resultsChan, &wg)
	}

	// Send jobs to the channel
	for _, job := range jobs {
		jobsChan <- job
	}
	close(jobsChan)

	// wait for all workers to finish and close results channel
	go func() {
		wg.Wait()
		close(resultsChan)
	}()

	// collect results and errors
	outputs := make(map[int]int)
	var errs []error
	for result := range resultsChan {
		if result.Err != nil {
			errs = append(errs, fmt.Errorf("job %d failed: %v", result.Job.ID, result.Err))
		} else {
			outputs[result.Job.ID] = result.Output
		}
	}

	return outputs, errs
}

func main() {
	jobs := []Job{
		{ID: 1, Input: 5},
		{ID: 2, Input: -3}, // invalid job
		{ID: 3, Input: 10},
	}

	outputs, errs := scheduler(jobs, 3) // 3 workers
	fmt.Println("Successful outouts:")
	for id, val := range outputs {
		fmt.Printf("Job %d: %d\n", id, val)
	}

	fmt.Println("\nErrors:")
	for _, err := range errs {
		fmt.Println(err)
	}
}
