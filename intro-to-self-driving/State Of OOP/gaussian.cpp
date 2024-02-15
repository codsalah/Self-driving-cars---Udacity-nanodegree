#include <cmath>  // Include the math library for math functions and constants
// Define M_PI manually if it's not defined
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// class declaration
class Gaussian {
private:
    float mu, sigma2;

public:
    // constructor functions
    Gaussian();
    Gaussian(float, float);

    // change value of average and standard deviation 
    void setMu(float);
    void setSigma2(float);

    // output value of average and standard deviation
    float getMu();
    float getSigma2();

    // functions to evaluate 
    float evaluate(float);
    Gaussian mul(Gaussian);
    Gaussian add(Gaussian);
};

// Constructor implementations
Gaussian::Gaussian() {
    mu = 0;
    sigma2 = 1;    
}

Gaussian::Gaussian(float average, float sigma) {
    mu = average;
    sigma2 = sigma;
}

// Setter implementations
void Gaussian::setMu(float average) {
    mu = average;
}

void Gaussian::setSigma2(float sigma) {
    sigma2 = sigma;
}

// Getter implementations
float Gaussian::getMu() {
    return mu;
}

float Gaussian::getSigma2() {
    return sigma2;
}

// Evaluation function implementation
float Gaussian::evaluate(float x) {
    float coefficient;
    float exponential;

    // Calculate coefficient and exponential parts of the Gaussian PDF
    coefficient = 1.0 / sqrt(2.0 * M_PI * sigma2);
    exponential = exp(-0.5 * pow((x - mu), 2) / sigma2);

    // Return the product of coefficient and exponential
    return coefficient * exponential;
}

// Multiplication function implementation
Gaussian Gaussian::mul(Gaussian other) {
    float denominator;
    float numerator;
    float new_mu;
    float new_var;

    // Calculate new mean and variance for the resulting Gaussian
    denominator = sigma2 + other.getSigma2();
    numerator = mu * other.getSigma2() + other.getMu() * sigma2;
    new_mu = numerator / denominator;

    new_var = 1.0 / ((1.0 / sigma2) + (1.0 / other.sigma2));

    // Return the resulting Gaussian
    return Gaussian(new_mu, new_var);
}

// Addition function implementation
Gaussian Gaussian::add(Gaussian other) {
    float new_mu;
    float new_sigma2;

    // Calculate new mean and variance for the resulting Gaussian
    new_mu = mu + other.getMu();
    new_sigma2 = sigma2 + other.getSigma2();

    // Return the resulting Gaussian
    return Gaussian(new_mu, new_sigma2);
}