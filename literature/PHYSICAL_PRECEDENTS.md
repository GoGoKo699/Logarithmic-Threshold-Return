# Physical precedents: what each source actually supports

**4 October 2026. Primary-source audit for the fixed lattice model.** This register
supports [ASSUMPTIONS.md](ASSUMPTIONS.md); it does not select a new platform, tutorial
or detector. The older access labels in the preserved PRIOR_ART.md remain historical.
A component precedent is not evidence that our complete protocol has been implemented.
Only the passages specified below were checked; no paper's experimental data or full
supplement has been independently reproduced.

## Y22 — closest joint subset, not the threshold experiment

A. W. Young et al., *Tweezer-programmable 2D quantum walks in a Hubbard-regime lattice*
(2022), [arXiv:2202.01204v1](https://arxiv.org/abs/2202.01204v1),
[published DOI](https://doi.org/10.1126/science.abo0608).
**Access:** [primary HTML](https://arxiv.org/html/2202.01204v1), main ground-state and
local-attraction passages; Methods I.1, I.2 and I.5. Publisher retrieval failed.

This experiment combines two-dimensional coherent motion, a local attractive
potential, and reversible ground-state loading. The loaded state uses broad Gaussian
confinement, not our single-site endpoint. Its spatial-distribution overlap is an
upper bound on state fidelity, not a phase certificate. Preparation filtering and
survival accounting are explicit. The authors distinguish imaging/cooling area from
walks and report curvature/inhomogeneity limitations. **Classification: jointly
demonstrated subset.** It neither measures our bound-state projector nor establishes
our quadratic cycle, residual-depth family, or coherent volume/time requirement.

**Control-pass access extension:** Methods I.2, I.3 and I.5, and Section II were
also checked. Alignment can change the effective oracle depth and address neighbors;
the supplement describes intensity-control dynamic range, higher-band filtering,
curvature, and a dynamical oracle-depth calibration. None supplies a uniform residual
certificate for our cycle. These are further passages of Y22, not a new source.

## J98 — single-band reduction and its hypotheses

D. Jaksch et al., *Cold bosonic atoms in optical lattices*, Physical Review Letters
**81**, 3108 (1998), [DOI](https://doi.org/10.1103/PhysRevLett.81.3108),
[arXiv:cond-mat/9805329](https://arxiv.org/abs/cond-mat/9805329).
**Access:** [primary PDF](https://arxiv.org/pdf/cond-mat/9805329), pp. 1–2 and
Eqs. (1)–(2), visually checked.

The Wannier expansion provides hopping and on-site terms under lowest-band and
energy-scale assumptions. Its smooth external-potential approximation is not
automatically valid for a tightly focused single-site perturbation.
**Classification: theoretical idealization with explicit reduction conditions.**
This supports the framework, not a calibrated optical realization of exactly one
negative diagonal entry with unchanged hopping.

## W11 — initialization, addressing, and band diagnostics

C. Weitenberg et al., *Single-Spin Addressing in an Atomic Mott Insulator* (2011),
[arXiv:1101.2076](https://arxiv.org/abs/1101.2076).
**Access:** [primary PDF](https://arxiv.org/pdf/1101.2076), pp. 3, 4 and 6 visually
checked; addressing, coherent tunneling and vibrational-excitation passages.

Focused light and microwave control initialize selected lattice atoms; coherent
tunneling provides a motional diagnostic. Beam pointing and addressing-induced
excitation affect band occupation. Position imaging follows freezing the motion.
**Classification: preparation, control and diagnostic components.** A spin-flip
fidelity is not a bound-orbital fidelity, and sub-site addressing resolution does
not imply a perfectly single-site scalar potential.

## K12 — three-dimensional motional preparation

A. M. Kaufman, B. J. Lester and C. A. Regal, *Cooling a single atom in an optical
tweezer to its quantum ground state*, Physical Review X **2**, 041014 (2012),
[DOI](https://doi.org/10.1103/PhysRevX.2.041014),
[arXiv:1209.2087v2](https://arxiv.org/abs/1209.2087v2).
**Access:** [primary HTML](https://arxiv.org/html/1209.2087v2), abstract and main
cooling, spectroscopy and initial-atom-selection passages.

Raman sideband cooling prepares three-dimensional motional ground-state population;
sideband spectroscopy and spin-motion control diagnose it. The cooling has an
explicit dissipative step. **Classification: preparation and motional-diagnostic
components.** Neither the tweezer eigenstate nor a temperature estimate establishes
the extended lattice state $`b_4`$. Pre-cycle cooling is not evidence for dissipation
being harmless during the threshold cycle.

## T12 — radial cooling is not a three-dimensional fidelity certificate

J. D. Thompson et al., *Coherence and Raman sideband cooling of a single atom in an
optical tweezer*, [arXiv:1209.3028v1](https://arxiv.org/abs/1209.3028v1) (2012);
related publication Physical Review Letters **110**, 133001 (2013),
[DOI](https://doi.org/10.1103/PhysRevLett.110.133001).
**Access:** [primary preprint HTML](https://arxiv.org/html/1209.3028v1), main text;
not the full published version.

The checked preprint diagnoses polarization-related internal-state decoherence and
uses bias-field control with Raman sideband cooling. Its radial occupation is near
zero while its axial occupation is about eight; these are not near-unit joint 3D
ground-state occupation. **Classification: preparation and spectroscopy components.**
Internal-state coherence is not a measured coherence time for a freely spreading
lattice orbital. Keep the preprint's actual axial limitation rather than paraphrasing
its abstract as a stronger cooling result.

## N18 — strontium cooling and detection in one apparatus

M. A. Norcia, A. W. Young and A. M. Kaufman, *Microscopic Control and Detection of
Ultracold Strontium in Optical-Tweezer Arrays*, Physical Review X **8**, 041054 (2018),
[DOI](https://doi.org/10.1103/PhysRevX.8.041054),
[arXiv:1810.06626](https://arxiv.org/abs/1810.06626).
**Access:** [primary PDF](https://arxiv.org/pdf/1810.06626), selected main-text
passages in Sections I–III; p. 2 visually checked. No full supplement audit.

State-insensitive trapping, narrow-line motional cooling, thermometry, and atom-presence
imaging are combined. The thermometry discussion retains uncertainty and possible
probe-induced changes. **Classification: joint preparation/detection components in
tweezers.** There is no threshold lattice cycle here; detecting whether a tweezer
contains an atom does not identify a particular extended lattice orbital.

## Z16 — beam shaping, with distinct optical and atomic calibrations

P. Zupancic et al., *Ultra-precise holographic beam shaping for microscopic quantum
control*, Optics Express **24**, 13881–13893 (2016),
[DOI](https://doi.org/10.1364/OE.24.013881),
[arXiv:1604.07653v2](https://arxiv.org/abs/1604.07653v2).
**Access:** [primary HTML](https://arxiv.org/html/1604.07653v2), Sections 3–6.

Holographic aberration control and atom-based calibration enable structured lattice
potentials and preparation of selected rows. The optical-bench intensity benchmark
and the in-apparatus calibration are different measurements. The demonstrated
microscope potentials are repulsive. **Classification: local-control and preparation
components.** Do not turn optical beam-profile precision into a measured residual
attractive on-site energy, or row preparation into preparation of $`b_4`$.

## S10 — site fluorescence and background confinement

J. F. Sherson et al., *Single-Atom Resolved Fluorescence Imaging of an Atomic Mott
Insulator* (2010), [arXiv:1006.3799v2](https://arxiv.org/abs/1006.3799v2).
**Access:** [primary PDF](https://arxiv.org/pdf/1006.3799), pp. 2–3 text;
p. 2, including Fig. 2 and the detection description, visually checked.

The lattice is deepened for fluorescence and optical molasses; light-assisted pair
loss makes the many-atom measurement parity-sensitive. Additional harmonic confinement
is part of the setup. **Classification: position-readout component.** In the single
particle sector parity reduces to occupation, but occupation is still not an orbital
projector. Imaging after pinning is not evidence for coherent, flat-lattice propagation
throughout the same field of view.

## B22 — a phase-sensitive motional diagnostic, not our detector

M. O. Brown et al., *Time-of-Flight Quantum Tomography of Single Atom Motion* (2022),
[arXiv:2203.03053v2](https://arxiv.org/abs/2203.03053v2).
**Access:** [primary PDF](https://arxiv.org/pdf/2203.03053), main text pp. 1–3;
pp. 2–3 visually checked. No full supplement or reconstruction-code audit.

Known trap evolution and time-of-flight distributions permit density-matrix/Wigner
reconstruction of single-atom motion. The demonstrated sequence includes preparation
filtering and depends on a calibrated motional model. **Classification: phase-sensitive
diagnostic component.** This shows why multiple controlled measurements contain more
information than one position histogram; it is not a calibrated two-dimensional
lattice bound-state projector or an adopted replacement detector.

## L13 — a moving basis changes the generator

M. Łącki and J. Zakrzewski, *Fast Dynamics for Atoms in Optical Lattices*, Physical
Review Letters **110**, 065301 (2013),
[DOI](https://doi.org/10.1103/PhysRevLett.110.065301),
[arXiv:1210.7957v2](https://arxiv.org/abs/1210.7957v2).
**Access:** [primary PDF](https://arxiv.org/pdf/1210.7957), pp. 1–2 visually checked,
including Eqs. (3)–(6); publisher bibliographic record checked. HTML was blocked.

The paper retains the derivative of the Wannier-basis transformation during lattice
changes. It also distinguishes finite-band and nearest-neighbor truncations. Its
parity-symmetric single-band correction vanishes; higher-band couplings need not.
**Classification: theoretical reduction/limitation precedent.** It does not prove
our local beam preserves a fixed band, nor supply an experimental error budget.
The date printed inside a reformatted copy is not substituted for the 2013 record.

## C18 — lattice-depth spectroscopy is not local-defect calibration

C. Cabrera-Gutiérrez et al., *Robust calibration of an optical-lattice depth based on
a phase shift*, Physical Review A **97**, 043617 (2018),
[DOI](https://doi.org/10.1103/PhysRevA.97.043617).
**Access:** [primary preprint HTML](https://arxiv.org/html/1801.08784v1), Sections
II–III, especially Eqs. (14)–(19). Its preprint title begins *Ultrarobust*; the
[abstract record](https://arxiv.org/abs/1801.08784) identifies the 2018 publication.

A phase shift populates Bloch bands; their energy differences determine dominant
oscillation frequencies used to infer lattice depth. The analysis goes beyond a
single-well Gaussian approximation. **Classification: band-spectrum calibration
component.** Calibrating the periodic lattice does not calibrate the added attractive
site or certify negligible higher-band effects during another protocol. No benchmark
from this method is assigned to our device, and its quench is not adopted here.

## M17 — finite-region potential compensation, not an infinite flat lattice

A. Mazurenko et al., *A cold-atom Fermi–Hubbard antiferromagnet*, Nature **545**,
462–466 (2017), [DOI](https://doi.org/10.1038/nature22362).
**Access:** [publisher primary page](https://www.nature.com/articles/nature22362),
Extended Data Fig. 1–2 captions and bibliographic record only. The full main-text
methods and preprint were not accessed successfully; this is a caption-level
primary record, not an abstract-only record or a complete paper audit.

The captions specify a shaped field compensating gradients and central curvature,
with walls surrounding a finite subsystem. **Classification: confinement-control
component in an interacting lattice.** Equilibrium density uniformity is not a
bound on our single-particle phase error, propagation time, or residual generator.
No many-body result is imported into the threshold theorem.

## Abstract-level comparators, excluded from detailed-access counts

**P15:** P. M. Preiss et al., *Strongly Correlated Quantum Walks in Optical Lattices*,
Science **347**, 1229–1233 (2015), [DOI](https://doi.org/10.1126/science.1260364),
[arXiv:1409.3100v2](https://arxiv.org/abs/1409.3100v2).
Primary abstract and author-group record checked; PDF/HTML retrieval attempts failed.
The abstract supports interacting quantum-walk experiments, not details of a claimed
single-particle preparation or measurement protocol in this audit.

**C15:** L. W. Cheuk et al., *A Quantum Gas Microscope for Fermionic Atoms*,
Physical Review Letters **114**, 193001 (2015),
[DOI](https://doi.org/10.1103/PhysRevLett.114.193001),
[arXiv:1503.02648v2](https://arxiv.org/abs/1503.02648v2).
Primary abstract checked; attempted full-text retrieval failed. It supplies a
fermionic-site-imaging precedent, not detailed proof of our motional readout.

## Access and counting policy

There are **twelve passage-level primary records and two abstract-only comparators**
here. M17 is limited to primary extended-data captions; L13 and C18 are the two new
main-text comparisons. The original nine access records are not upgraded wholesale.
One article appearing under several applicable premises is still one article.
Reformatted HTML dates are not publication dates; the cited preprint versions and
bibliographic records determine those dates. Failed retrievals, reviews, unrelated
search hits, and internal-spin-only addressing examples are not promoted to extra
motional-control evidence. Third-party PDFs are neither committed nor redistributed.

For the six preparation-component and seven measurement/diagnostic-component records
used in the matrix, the five-to-ten *component* target is met. The target is **not** met
for demonstrated exact preparation/readout of this model, nor for every other premise.
Those shortfalls and the absence of a joint protocol remain explicit in ASSUMPTIONS.md.
Further retrieval attempts did not make P15 a full-text record; its count is unchanged.
The [model-residual test](../research/MODEL_RESIDUAL.md) states what the remaining
model-specific calibration must establish. No further generic source expansion is
required merely to turn an unresolved implementation row into a larger citation count.
